from flask import Flask, render_template

pkmn_from_index = [0, 112, 115, 32, 35, 21, 100, 34, 80, 2, 103, 108, 102,
                   88, 94, 29, 31, 104, 111, 131, 59, 151, 130, 90, 72, 92, 123,
                   120, 9, 127, 114, 152, 152, 58, 95, 22, 16, 79, 64, 75, 113,
                   67, 122, 106, 107, 24, 47, 54, 96, 76, 152, 126, 152, 125,
                   82, 109, 152, 56, 86, 50, 128, 152, 152, 152, 83, 48, 149,
                   152, 152, 152, 84, 60, 124, 146, 144, 145, 132, 52, 98, 152,
                   152, 152, 37, 38, 25, 26, 152, 152, 147, 148, 140, 141, 116,
                   117, 152, 152, 27, 28, 138, 139, 39, 40, 133, 136, 135, 134,
                   66, 41, 23, 46, 61, 62, 13, 14, 15, 152, 85, 57, 51, 49, 87,
                   152, 152, 10, 11, 12, 68, 152, 55, 97, 42, 150, 143, 129,
                   152, 152, 89, 152, 99, 91, 152, 101, 36, 110, 53, 105, 152,
                   93, 63, 65, 17, 18, 121, 1, 3, 73, 152, 118, 119, 152, 152,
                   152, 152, 77, 78, 19, 20, 33, 30, 74, 137, 142, 152, 81, 152,
                   152, 4, 7, 5, 8, 6, 152, 152, 152, 152, 43, 44, 45, 69, 70,
                   71]

app = Flask(__name__)

@app.route('/')
def list_games():
    return render_template('list.html')

@app.route('/gr')
def green():
    return render_template('viewer.html', nb=151, folder='gr')

@app.route('/rb')
def redblue():
    return render_template('viewer.html', nb=151, folder='rb')

@app.route('/y')
def yellow():
    return render_template('viewer.html', nb=151, folder='y')

@app.route('/g')
def gold():
    return render_template('viewer.html', nb=251, folder='g')

@app.route('/s')
def silver():
    return render_template('viewer.html', nb=251, folder='s')

@app.route('/c')
def crystal():
    return render_template('viewer.html', nb=251, folder='c')

@app.route('/agb')
def agb():
    return render_template('viewer.html', nb=386, folder='agb')

@app.route('/frlg')
def frlg():
    return render_template('viewer.html', nb=386, folder='frlg')

@app.route('/dpp')
def dpp():
    return render_template('viewer.html', nb=493, folder='dpp')

@app.route('/hgss')
def hgss():
    return render_template('viewer.html', nb=493, folder='hgss')

@app.route('/bw')
def bw():
    return render_template('viewer.html', nb=649, folder='bw')


@app.route('/_update', methods=['GET', 'POST'])
def update():
    string = ''
    with open('pkdx_memory.txt', 'r') as f:
        for line in f:
            string += format(int(line), '08b')[::-1]
    return string

@app.route('/_update_road', methods=['GET', 'POST'])
def update_road():
    string = ''
    is_level = True
    with open('pkmns_road.txt', 'r') as f:
        not_in_town = int(f.readline())
        if not_in_town:
            for w in f:
                if is_level:
                    string += 'level.{} '.format(w)
                else:
                    string += str(pkmn_from_index[int(w)]) + ' '
                is_level ^= True
    return string


if __name__ == '__main__':
    app.run(
        host = '0.0.0.0',
        port = 80,
        debug = True
    )


'''
TODO:
-crop white around pkmn
-update line count
-lua
-unown Mode
-sex mode?
-shiney mode?
-show which pkmn appears on your road

fire red $44E850
ruby $3B1874
'''
