import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang17_p1_b4_c1_ds12(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','6']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                x=randint(1,6)
                y=-x
                tcn=x
                tcd=-x


                du = ['$(0;%s)$'%(latex(y)),
                    ]
                da= random.choice(du)
                s = ['$(0;%s)$'%(latex(y+1)),
                    '$(%s;0)$'%(latex(y)),
                    '$(%s;%s)$'%(latex(x-1),latex(y))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi =('\\immini{'
                                'Cho hàm số $y=\\dfrac{ax+b}{cx+d}$ có đồ thị như hình vẽ bên. Toạ độ giao điểm của đồ thị hàm số đã cho với trục tung là'
                            '}{'
                            '\\scalebox{0.6}{ ' 
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                            '\\def\\a{1} \\def\\b{-1} \\def\\c{1} \\def\\d{1}\n' 
                '\\def\\xmin{-5} \\def\\xmax{4}\n'
                '\\def\\ymin{-3} \\def\\ymax{4}\n'
                '\\draw[->] (\\xmin,0)--(\\xmax,0) node [below]{$x$};\n'
                '\\draw[->] (0,\\ymin)--(0,\\ymax) node [left]{$y$};\n'
                '\\node at (0,0) [below left]{$O$};\n'
                '\\clip (\\xmin+0.1,\\ymin+0.1) rectangle (\\xmax-0.1,\\ymax-0.1);\n'
                '\\draw[smooth,samples=300,domain=\\xmin:(-\\d/\\c-0.1)] plot(\\x,{(\\a*(\\x)+\\b)/(\\c*(\\x)+\\d)});\n'
                '\\draw[smooth,samples=300,domain=(-\\d/\\c+0.1:\\xmax)] plot(\\x,{(\\a*(\\x)+\\b)/(\\c*(\\x)+\\d)});\n'
                '\\draw (-\\d/\\c,\\ymin)--(-\\d/\\c,\\ymax);\n'
                '\\draw (\\xmin,\\a/\\c)--(\\xmax,\\a/\\c);\n'
                '\\draw (-\\b/\\a,0) node[above] {$%s$};\n'
                '\\draw (0,\\b/\\d) node[right] {$%s$};\n'
                '\\draw (0,\\a/\\c) node[above right] {$%s$};\n'
                '\\draw (-\\d/\\c,0) node[below left] {$%s$};\n'
                    '\\end{tikzpicture}}}\n'

                        %(latex(x),latex(y),latex(tcn),latex(tcd)))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai= ('Từ đồ thị ta thấy giao điểm của đồ thị hàm số với trục tung có tọa độ là $(0;%s)$.'
                        %(latex(y)

                            )

                        )
            if dang=='2':
                # Khai báo biến
                x1=randint(1,5)
                x=2*x1
                y=-2*x1
                tcn=x1
                tcd=-x1


                du = ['$(0;%s)$'%(latex(y)),
                    ]
                da= random.choice(du)
                s = ['$(0;%s)$'%(latex(y+1)),
                    '$(%s;0)$'%(latex(y)),
                    '$(%s;%s)$'%(latex(x-1),latex(y))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi =('\\immini{'
                                'Cho hàm số $y=\\dfrac{ax+b}{cx+d}$ có đồ thị như hình vẽ bên. Toạ độ giao điểm của đồ thị hàm số đã cho với trục tung là'
                            '}{'
                            '\\scalebox{0.6}{ ' 
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                            '\\def\\a{1} \\def\\b{-2} \\def\\c{1} \\def\\d{1}\n' 
                '\\def\\xmin{-4} \\def\\xmax{5}\n'
                '\\def\\ymin{-4} \\def\\ymax{4}\n'
                '\\draw[->] (\\xmin,0)--(\\xmax,0) node [below]{$x$};\n'
                '\\draw[->] (0,\\ymin)--(0,\\ymax) node [left]{$y$};\n'
                '\\node at (0,0) [below left]{$O$};\n'
                '\\clip (\\xmin+0.1,\\ymin+0.1) rectangle (\\xmax-0.1,\\ymax-0.1);\n'
                '\\draw[smooth,samples=300,domain=\\xmin:(-\\d/\\c-0.1)] plot(\\x,{(\\a*(\\x)+\\b)/(\\c*(\\x)+\\d)});\n'
                '\\draw[smooth,samples=300,domain=(-\\d/\\c+0.1:\\xmax)] plot(\\x,{(\\a*(\\x)+\\b)/(\\c*(\\x)+\\d)});\n'
                '\\draw (-\\d/\\c,\\ymin)--(-\\d/\\c,\\ymax);\n'
                '\\draw (\\xmin,\\a/\\c)--(\\xmax,\\a/\\c);\n'
                '\\draw (-\\b/\\a,0) node[above] {$%s$};\n'
                '\\draw (0,\\b/\\d) node[right] {$%s$};\n'
                '\\draw (0,\\a/\\c) node[above right] {$%s$};\n'
                '\\draw (-\\d/\\c,0) node[below left] {$%s$};\n'
                    '\\end{tikzpicture}}}\n'

                        %(latex(x),latex(y),latex(tcn),latex(tcd)))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai= ('Từ đồ thị ta thấy giao điểm của đồ thị hàm số với trục tung có tọa độ là $(0;%s)$.'
                        %(latex(y)

                            )

                        )
            if dang=='3':
                # Khai báo biến
                x=randint(1,6)
                y=-x
                tcn=x
                tcd=-x


                du = ['$(%s;0)$'%(latex(x)),
                    ]
                da= random.choice(du)
                s = ['$(0;%s)$'%(latex(x)),
                    '$(%s;0)$'%(latex(x-1)),
                    '$(%s;%s)$'%(latex(x),latex(y+1))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi =('\\immini{'
                                'Cho hàm số $y=\\dfrac{ax+b}{cx+d}$ có đồ thị như hình vẽ bên. Toạ độ giao điểm của đồ thị hàm số đã cho với trục hoành là'
                            '}{'
                            '\\scalebox{0.6}{ ' 
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                            '\\def\\a{1} \\def\\b{-1} \\def\\c{1} \\def\\d{1}\n' 
                '\\def\\xmin{-5} \\def\\xmax{4}\n'
                '\\def\\ymin{-3} \\def\\ymax{4}\n'
                '\\draw[->] (\\xmin,0)--(\\xmax,0) node [below]{$x$};\n'
                '\\draw[->] (0,\\ymin)--(0,\\ymax) node [left]{$y$};\n'
                '\\node at (0,0) [below left]{$O$};\n'
                '\\clip (\\xmin+0.1,\\ymin+0.1) rectangle (\\xmax-0.1,\\ymax-0.1);\n'
                '\\draw[smooth,samples=300,domain=\\xmin:(-\\d/\\c-0.1)] plot(\\x,{(\\a*(\\x)+\\b)/(\\c*(\\x)+\\d)});\n'
                '\\draw[smooth,samples=300,domain=(-\\d/\\c+0.1:\\xmax)] plot(\\x,{(\\a*(\\x)+\\b)/(\\c*(\\x)+\\d)});\n'
                '\\draw (-\\d/\\c,\\ymin)--(-\\d/\\c,\\ymax);\n'
                '\\draw (\\xmin,\\a/\\c)--(\\xmax,\\a/\\c);\n'
                '\\draw (-\\b/\\a,0) node[above] {$%s$};\n'
                '\\draw (0,\\b/\\d) node[right] {$%s$};\n'
                '\\draw (0,\\a/\\c) node[above right] {$%s$};\n'
                '\\draw (-\\d/\\c,0) node[below left] {$%s$};\n'
                    '\\end{tikzpicture}}}\n'

                        %(latex(x),latex(y),latex(tcn),latex(tcd)))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai= ('Từ đồ thị ta thấy giao điểm của đồ thị hàm số với trục hoành có tọa độ là $(%s;0)$.'
                        %(latex(x)

                            ))
            if dang=='4':
                # Khai báo biến
                x1=randint(1,5)
                x=2*x1
                y=-2*x1
                tcn=x1
                tcd=-x1


                du = ['$(%s;0)$'%(latex(x)),
                    ]
                da= random.choice(du)
                s = ['$(0;%s)$'%(latex(x)),
                    '$(%s;0)$'%(latex(x-1)),
                    '$(%s;%s)$'%(latex(x),latex(y+1))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi =('\\immini{'
                                'Cho hàm số $y=\\dfrac{ax+b}{cx+d}$ có đồ thị như hình vẽ bên. Toạ độ giao điểm của đồ thị hàm số đã cho với trục hoành là'
                            '}{'
                            '\\scalebox{0.6}{ ' 
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                            '\\def\\a{1} \\def\\b{-2} \\def\\c{1} \\def\\d{1}\n' 
                '\\def\\xmin{-5} \\def\\xmax{4}\n'
                '\\def\\ymin{-3} \\def\\ymax{4}\n'
                '\\draw[->] (\\xmin,0)--(\\xmax,0) node [below]{$x$};\n'
                '\\draw[->] (0,\\ymin)--(0,\\ymax) node [left]{$y$};\n'
                '\\node at (0,0) [below left]{$O$};\n'
                '\\clip (\\xmin+0.1,\\ymin+0.1) rectangle (\\xmax-0.1,\\ymax-0.1);\n'
                '\\draw[smooth,samples=300,domain=\\xmin:(-\\d/\\c-0.1)] plot(\\x,{(\\a*(\\x)+\\b)/(\\c*(\\x)+\\d)});\n'
                '\\draw[smooth,samples=300,domain=(-\\d/\\c+0.1:\\xmax)] plot(\\x,{(\\a*(\\x)+\\b)/(\\c*(\\x)+\\d)});\n'
                '\\draw (-\\d/\\c,\\ymin)--(-\\d/\\c,\\ymax);\n'
                '\\draw (\\xmin,\\a/\\c)--(\\xmax,\\a/\\c);\n'
                '\\draw (-\\b/\\a,0) node[above] {$%s$};\n'
                '\\draw (0,\\b/\\d) node[right] {$%s$};\n'
                '\\draw (0,\\a/\\c) node[above right] {$%s$};\n'
                '\\draw (-\\d/\\c,0) node[below left] {$%s$};\n'
                    '\\end{tikzpicture}}}\n'

                        %(latex(x),latex(y),latex(tcn),latex(tcd)))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai= ('Từ đồ thị ta thấy giao điểm của đồ thị hàm số với trục hoành có tọa độ là $(%s;0)$.'
                        %(latex(x)

                            )

                        )
            if dang=='5':
                # Khai báo biến
                x=randint(-6,-1)
                y=x
                tcn=-nsimplify(x/2)
                tcd=-nsimplify(x/2)


                du = ['$(0;%s)$'%(latex(y)),
                    ]
                da= random.choice(du)
                s = ['$(0;%s)$'%(latex(y+1)),
                    '$(%s;0)$'%(latex(y)),
                    '$(%s;%s)$'%(latex(x),latex(y+1))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi =('\\immini{'
                                'Cho hàm số $y=\\dfrac{ax+b}{cx+d}$ có đồ thị như hình vẽ bên. Toạ độ giao điểm của đồ thị hàm số đã cho với trục tung là'
                            '}{'
                            '\\scalebox{0.6}{ ' 
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                            '\\def\\a{1} \\def\\b{2} \\def\\c{1} \\def\\d{-1}\n' 
                '\\def\\xmin{-5} \\def\\xmax{4}\n'
                '\\def\\ymin{-3} \\def\\ymax{4}\n'
                '\\draw[->] (\\xmin,0)--(\\xmax,0) node [below]{$x$};\n'
                '\\draw[->] (0,\\ymin)--(0,\\ymax) node [left]{$y$};\n'
                '\\node at (0,0) [below left]{$O$};\n'
                '\\clip (\\xmin+0.1,\\ymin+0.1) rectangle (\\xmax-0.1,\\ymax-0.1);\n'
                '\\draw[smooth,samples=300,domain=\\xmin:(-\\d/\\c-0.1)] plot(\\x,{(\\a*(\\x)+\\b)/(\\c*(\\x)+\\d)});\n'
                '\\draw[smooth,samples=300,domain=(-\\d/\\c+0.1:\\xmax)] plot(\\x,{(\\a*(\\x)+\\b)/(\\c*(\\x)+\\d)});\n'
                '\\draw (-\\d/\\c,\\ymin)--(-\\d/\\c,\\ymax);\n'
                '\\draw (\\xmin,\\a/\\c)--(\\xmax,\\a/\\c);\n'
                '\\draw (-\\b/\\a,0) node[above] {$%s$};\n'
                '\\draw (0,\\b/\\d) node[right] {$%s$};\n'
                '\\draw (0,\\a/\\c) node[above right] {$%s$};\n'
                '\\draw (-\\d/\\c,0) node[below left] {$%s$};\n'
                    '\\end{tikzpicture}}}\n'

                        %(latex(x),latex(y),latex(tcn),latex(tcd)))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai= ('Từ đồ thị ta thấy giao điểm của đồ thị hàm số với trục tung có tọa độ là $(0;%s)$.'
                        %(latex(y)

                            )

                        )
            if dang=='6':
                # Khai báo biến
                x=randint(-6,-1)
                y=x
                tcn=-nsimplify(x/2)
                tcd=-nsimplify(x/2)


                du = ['$(%s;0)$'%(latex(x)),
                    ]
                da= random.choice(du)
                s = ['$(0;%s)$'%(latex(x)),
                    '$(%s;0)$'%(latex(x-1)),
                    '$(%s;%s)$'%(latex(x-1),latex(y))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi =('\\immini{'
                                'Cho hàm số $y=\\dfrac{ax+b}{cx+d}$ có đồ thị như hình vẽ bên. Toạ độ giao điểm của đồ thị hàm số đã cho với trục hoành là'
                            '}{'
                            '\\scalebox{0.6}{ ' 
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                            '\\def\\a{1} \\def\\b{2} \\def\\c{1} \\def\\d{-1}\n' 
                '\\def\\xmin{-5} \\def\\xmax{4}\n'
                '\\def\\ymin{-3} \\def\\ymax{4}\n'
                '\\draw[->] (\\xmin,0)--(\\xmax,0) node [below]{$x$};\n'
                '\\draw[->] (0,\\ymin)--(0,\\ymax) node [left]{$y$};\n'
                '\\node at (0,0) [below left]{$O$};\n'
                '\\clip (\\xmin+0.1,\\ymin+0.1) rectangle (\\xmax-0.1,\\ymax-0.1);\n'
                '\\draw[smooth,samples=300,domain=\\xmin:(-\\d/\\c-0.1)] plot(\\x,{(\\a*(\\x)+\\b)/(\\c*(\\x)+\\d)});\n'
                '\\draw[smooth,samples=300,domain=(-\\d/\\c+0.1:\\xmax)] plot(\\x,{(\\a*(\\x)+\\b)/(\\c*(\\x)+\\d)});\n'
                '\\draw (-\\d/\\c,\\ymin)--(-\\d/\\c,\\ymax);\n'
                '\\draw (\\xmin,\\a/\\c)--(\\xmax,\\a/\\c);\n'
                '\\draw (-\\b/\\a,0) node[above] {$%s$};\n'
                '\\draw (0,\\b/\\d) node[right] {$%s$};\n'
                '\\draw (0,\\a/\\c) node[above right] {$%s$};\n'
                '\\draw (-\\d/\\c,0) node[below left] {$%s$};\n'
                    '\\end{tikzpicture}}}\n'

                        %(latex(x),latex(y),latex(tcn),latex(tcd)))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai= ('Từ đồ thị ta thấy giao điểm của đồ thị hàm số với trục hoành có tọa độ là $(%s;0)$.'
                        %(latex(y)

                            )

                        )



            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
            return content

