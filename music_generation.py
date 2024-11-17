# Passo 1: Importações
import numpy as np
from music21 import converter, instrument, note, chord, stream
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout, Input
from tensorflow.keras.optimizers import Adam

# Passo 2: Carregar o arquivo MIDI
midi = converter.parse("midi_files/music.mid")

# Passo 3: Processamento das notas
notes = []
for element in midi.flatten().notes:  
    if isinstance(element, note.Note):
        notes.append(str(element.pitch))
    elif isinstance(element, chord.Chord):
        notes.append('.'.join(str(n) for n in element.normalOrder))

# Passo 4: Codificação das notas
note_names = sorted(set(notes))
note_to_int = dict((note, number) for number, note in enumerate(note_names))

# Passo 5: Preparar os dados de entrada
sequence_length = 100
network_input = []
network_output = []
for i in range(len(notes) - sequence_length):
    seq_in = notes[i:i + sequence_length]
    seq_out = notes[i + sequence_length]
    
    # Converte seq_in e seq_out usando note_to_int
    network_input.append([note_to_int[char] for char in seq_in if char in note_to_int])
    if seq_out in note_to_int:  # Verifica se a nota de saída está no dicionário
        network_output.append(note_to_int[seq_out])

# Verificar se há entradas válidas
if len(network_input) == 0 or len(network_output) == 0:
    raise ValueError("Os dados de entrada ou saída estão vazios. Verifique o arquivo MIDI e o processamento.")

# Passo 6: Reformatar os dados para LSTM
X = np.reshape(network_input, (len(network_input), sequence_length, 1))
X = X / float(len(note_names))  
y = np.zeros((len(network_output), len(note_names)))
for i, seq in enumerate(network_output):
    y[i][seq] = 1

# Passo 7: Construção do modelo LSTM
model = Sequential([
    Input(shape=(X.shape[1], X.shape[2])),
    LSTM(512, return_sequences=True),
    Dropout(0.3),
    LSTM(512, return_sequences=True),
    Dropout(0.3),
    LSTM(512),
    Dense(256),
    Dropout(0.3),
    Dense(len(note_names), activation='softmax')
])
model.compile(loss='categorical_crossentropy', optimizer=Adam(learning_rate=0.001))

# Passo 8: Treinamento do modelo
model.fit(X, y, epochs=200, batch_size=64)

# Passo 9: Gerar música com o modelo treinado
start_sequence = network_input[0]
prediction_input = start_sequence[:]
prediction_output = []

for _ in range(500):  # Gerar 500 notas
    prediction_input_reshaped = np.reshape(prediction_input, (1, len(prediction_input), 1))
    prediction_input_reshaped = prediction_input_reshaped / float(len(note_names))
    predicted_note = model.predict(prediction_input_reshaped, verbose=0)
    index = np.argmax(predicted_note)
    result = note_names[index]
    prediction_output.append(result)
    prediction_input.append(index)  # Adicionar índice ao invés de nota
    prediction_input = prediction_input[1:]  # Remover o primeiro elemento

# Converter as notas para um arquivo MIDI
stream_output = stream.Stream()
for pattern in prediction_output:
    if '.' in pattern or pattern.isdigit():
        chord_notes = [note.Note(int(n)) for n in pattern.split('.')]
        chord_output = chord.Chord(chord_notes)
        stream_output.append(chord_output)
    else:
        stream_output.append(note.Note(pattern))

# Salvar como arquivo MIDI
stream_output.write('midi', fp='generated_music.mid')
