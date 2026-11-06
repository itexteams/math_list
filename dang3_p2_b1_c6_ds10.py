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


def bt_dang3_p2_b1_c6_ds10(self):
            # Khai báo biến
            a = randint(20,63)
            if a==36:
                a = randint(20,63)
            b = randint(1,36)
            if b==6:
                b = randint(1,36)
            c = randint(1,36)
            if c==11:
                c = randint(1,36)
            d = randint(1,36)
            if d==6:
                d = randint(1,36)
            e = randint(1,36)
            if e==18:
                e = randint(1,36)
            f = randint(1,36)
            if f==12:
                f = randint(1,36)
            g = randint(1,36)
            if g==9:
                g = randint(1,36)
            h = randint(1,36)
            if h==15:
                h = randint(1,36)
            k = randint(1,36)
            if k==6:
                k = randint(1,36)
            # Nội dung câu hỏi
            noidungcauhoi = '''Gieo một con xúc xắc cân đối và đồng chất hai lần. \n'''

            # Các đáp án
            da_1_d = '\\True Số phần tử của không gian mẫu là $36$'
            da_1_s = 'Số phần tử của không gian mẫu là $%s$'%(latex(a))
            list_da_1=[da_1_d,da_1_s]
            da_1=random.choice(list_da_1)

            da_2_d = '\\True Số phần tử của biến cố $A:$"Hai lần xuất hiện mặt có số chấm bằng nhau" là $6$'
            da_2_s = 'Số phần tử của biến cố $A:$"Hai lần xuất hiện mặt có số chấm bằng nhau" là $%s$'%(latex(b))
            list_da_2=[da_2_d,da_2_s]
            da_2=random.choice(list_da_2)

            da_3_d = '\\True Số phần tử của biến cố $B:$"Ít nhất một lần xuất hiện mặt $2$ chấm" là $11$'
            da_3_s = 'Số phần tử của biến cố $B:$"Ít nhất một lần xuất hiện mặt hai chấm" là $%s$'%(latex(c))
            list_da_3=[da_3_d,da_3_s]
            da_3=random.choice(list_da_3)

            da_4_d = '\\True Số phần tử của biến cố $C:$"Mặt $5$ chấm xuất hiện lần đầu" là $6$'
            da_4_s = 'Số phần tử của biến cố $C:$"Mặt $5$ chấm xuất hiện lần đầu" là $%s$'%(latex(d))
            list_da_4=[da_4_d,da_4_s]
            da_4=random.choice(list_da_4)

            da_5_d = '\\True Số phần tử của biến cố $D:$"Tổng số chấm xuất hiện là một số chẵn" là $18$'
            da_5_s = 'Số phần tử của biến cố $D:$"Tổng số chấm xuất hiện là một số chẵn" là $%s$'%(latex(e))
            list_da_5=[da_5_d,da_5_s]
            da_5=random.choice(list_da_5)

            da_6_d = '\\True Số phần tử của biến cố $E:$"Tổng số chấm xuất hiện chia hết cho $3$" là $12$'
            da_6_s = 'Số phần tử của biến cố $E:$"Tổng số chấm xuất hiện chia hết cho $3$" là $%s$'%(latex(f))
            list_da_6=[da_6_d,da_6_s]
            da_6=random.choice(list_da_6)

            da_7_d = '\\True Số phần tử của biến cố $F:$"Tích số chấm xuất hiện là một số lẻ" là $9$'
            da_7_s = 'Số phần tử của biến cố $F:$"Tích số chấm xuất hiện là một số lẻ" là $%s$'%(latex(g))
            list_da_7=[da_7_d,da_7_s]
            da_7=random.choice(list_da_7)

            da_8_d = '\\True Số phần tử của biến cố $G:$"Số chấm ở lần tung thứ hai lớn hơn lần một" là $15$'
            da_8_s = 'Số phần tử của biến cố $G:$"Số chấm ở lần tung thứ hai lớn hơn lần một" là $%s$'%(latex(h))
            list_da_8=[da_8_d,da_8_s]
            da_8=random.choice(list_da_8)

            da_9_d = '\\True Số phần tử của biến cố $H:$"Tích số chấm xuất hiện là một số nguyên tố" là $6$'
            da_9_s = 'Số phần tử của biến cố $H:$"Tích số chấm xuất hiện là một số nguyên tố" là $%s$'%(latex(k))
            list_da_9=[da_9_d,da_9_s]
            da_9=random.choice(list_da_9)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_1, da_2, da_3, da_4, da_5, da_6, da_7, da_8, da_9]

            # Nội dung lời giải
            loigiai_1 = ('Không gian mẫu $\\Omega = \\left \\lbrace (i;j) | 1 \\le i; j \\le 6 \\right \\rbrace$. \\\\ \n'
                        'Do đó, số phần tử của không gian mẫu là $n(\\Omega)=6 \\cdot 6 =36$.'
                        )
            loigiai_2 = ('Ta có $A=\\left \\lbrace (1;1), (2;2), (3;3), (4;4), (5;5), (6;6) \\right \\rbrace$.\\\\ \n'
                        'Suy ra $n(A)=6$.'
                        )
            loigiai_3 = ('Ta có $B=\\left \\lbrace (1;2), (2;1), (2;2), (2;3), (2;4), (2;5), (2;6), (3;2), (4;2), (5;2), (6;2) \\right \\rbrace$.\\\\ \n'
                        'Suy ra $n(B)=11$.'
                        )
            loigiai_4 = ('Ta có $C=\\left \\lbrace (5;1), (5;2), (5;3), (5;4), (5;5) \\right \\rbrace$.\\\\ \n'
                        'Suy ra $n(C)=6$.'
                        )
            loigiai_5 = ('Ta có $D=\\big\\{ (1;1),(1;3),(1;5),(2;2),(2;4),(2;6),(3;1),(3;3),(3;5), \\\\ (4;2),(4;4),(4;6),(5;1),(5;3),(5;5),(6;2),(6;4),(6;6) \\big\\}$.\\\\ \n'
                        'Suy ra $n(D)=18$.'
                        )
            loigiai_6 = ('Ta có $E=\\left \\lbrace (1;2), (1;5), (2;1), (2;4), (3;3), (3;6), (4;2), (4;5), (5;1), (5;4), (6;3), (6;6) \\right \\rbrace$.\\\\ \n'
                        'Suy ra $n(E)=12$.'
                        )
            loigiai_7 = ('Ta có $F=\\left \\lbrace (1;1), (1;3), (1;5), (3;1), (3;3), (3;5), (5;1), (5;3), (5;5) \\right \\rbrace$.\\\\ \n'
                        'Suy ra $n(F)=9$.'
                        )
            loigiai_8 = ('Ta có $G=\\big\\{ (1;2), (1;3), (1;4), (1;5), (1;6), (2;3), (2;4), (2;5), (2;6), \\\\ (3;4), (3;5), (3;6), (4;5), (4;6), (5;6) \\big\\}$.\\\\ \n'
                        'Suy ra $n(G)=15$.'
                        )
            loigiai_9 = ('Ta có $H=\\big\\{ (1;2), (2;1), (1;3), (1;5), (3;1), (5;1) \\big\\}$.\\\\ \n'
                        'Suy ra $n(H)=6$.'
                        )
            # Đưa các lời giải vào danh sách lời giải
            list_2 = [loigiai_1, loigiai_2, loigiai_3, loigiai_4, loigiai_5, loigiai_6, loigiai_7, loigiai_8, loigiai_9]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined = list(zip(list_1, list_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers, shuffled_solutions = zip(*combined)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(shuffled_answers[0])+'}\n'
                '{'+str(shuffled_answers[1])+'}\n'
                '{'+str(shuffled_answers[2])+'}\n'
                '{'+str(shuffled_answers[3])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions[0])+'\n'
                '\\item '+str(shuffled_solutions[1])+'\n'
                '\\item '+str(shuffled_solutions[2])+'\n'
                '\\item '+str(shuffled_solutions[3])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

