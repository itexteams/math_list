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


def bt_dang1_p2_b1_c6_ds10(self):
            # Khai báo biến
            a = randint(1,5)
            b = randint(1,6)
            if b==3:
                b = randint(1,6)
            c = randint(1,6)
            if c==2:
                c = randint(1,6)
            d = randint(1,6)
            if d==5:
                d = randint(1,6)
            e = randint(1,6)
            if e==3:
                e = randint(1,6)
            f = randint(2,6)
            f1 = randint(1,6)
            if f1==f-1:
                f1 = randint(1,6)
            f2=set(range(1, f))

            g=randint(1,5)
            g1=randint(1,6)
            if g1==7-g:
                g1=randint(1,6)
            for i in range(1, 7-g):
                g2=set(range(g, g+i+1))
            # Nội dung câu hỏi
            noidungcauhoi = '''Gieo một con xúc xắc cân đối và đồng chất một lần.'''

            # Các đáp án
            da_1_d = '\\True Số phần tử của không gian mẫu là $6$'
            da_1_s = 'Số phần tử của không gian mẫu là $%s$'%(latex(a))
            list_da_1=[da_1_d,da_1_s]
            da_1=random.choice(list_da_1)

            da_2_d = '\\True Có $3$ khả năng xuất hiện mặt có số chấm lẻ'
            da_2_s = 'Có $%s$ khả năng xuất hiện mặt có số chấm lẻ'%(latex(b))
            list_da_2=[da_2_d,da_2_s]
            da_2=random.choice(list_da_2)

            da_3_d = '\\True Có $2$ khả năng xuất hiện mặt có số chấm chia hết cho $3$'
            da_3_s = 'Có $%s$ khả năng xuất hiện mặt có số chấm chia hết cho $3$'%(latex(c))
            list_da_3=[da_3_d,da_3_s]
            da_3=random.choice(list_da_3)

            da_4_d = '\\True Có $1$ khả năng xuất hiện mặt có số chấm chia hết cho $5$'
            da_4_s = 'Có $%s$ khẳ năng xuất hiện mặt có số chấm chia hết cho $5$'%(latex(d))
            list_da_4=[da_4_d,da_4_s]
            da_4=random.choice(list_da_4)

            da_5_d = '\\True Có $3$ khả năng xuất hiện mặt có số chấm là số nguyên tố'
            da_5_s = 'Có $%s$ khả năng xuất hiện mặt có số chấm là số nguyên tố'%(latex(e))
            list_da_5=[da_5_d,da_5_s]
            da_5=random.choice(list_da_5)

            da_6_d = '\\True Có $%s$ khả năng xuất hiện mặt có số chấm nhỏ hơn $%s$'%(latex(f-1),latex(f))
            da_6_s = 'Có $%s$ khả năng xuất hiện mặt có số chấm nhỏ hơn $%s$'%(latex(f1),latex(f))
            list_da_6=[da_6_d,da_6_s]
            da_6=random.choice(list_da_6)

            da_7_d = '\\True Có $%s$ khả năng xuất hiện mặt có số chấm không nhỏ hơn $%s$'%(latex(7-g),latex(g))
            da_7_s = 'Có $%s$ khả năng xuất hiện mặt có số chấm không nhỏ hơn $%s$'%(latex(g1),latex(g))
            list_da_7=[da_7_d,da_7_s]
            da_7=random.choice(list_da_7)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_1, da_2, da_3, da_4, da_5, da_6, da_7]

            # Nội dung lời giải
            loigiai_1 = ('Không gian mẫu $\\Omega = \\left \\lbrace 1;2;3;4;5;6 \\right \\rbrace$. \n'
                        'Do đó, số phần tử của không gian mẫu là $n(\\Omega)=6$.'
                        )
            loigiai_2 = ('Gọi biến cố $A:$"Mặt xuất hiện số chấm lẻ".\n'
                        'Ta có $A= \\left \\lbrace 1;3;5 \\right \\rbrace$ nên $n(A)=3$.'
                        )
            loigiai_3 = ('Gọi biến cố $B:$"Mặt xuất hiện số chấm chia hết cho $3$".\n'
                        'Ta có $B= \\left \\lbrace 3;6 \\right \\rbrace$ nên $n(B)=2$.'
                        )
            loigiai_4 = ('Gọi biến cố $C:$"Mặt xuất hiện số chấm chia hết cho $5$".\n'
                        'Ta có $C= \\left \\lbrace 5 \\right \\rbrace$ nên $n(C)=1$.'
                        )
            loigiai_5 = ('Gọi biến cố $D:$"Mặt xuất hiện số chấm là số nguyên tố".\n'
                        'Ta có $D= \\left \\lbrace 2;3;5 \\right \\rbrace$ nên $n(D)=3$.'
                        )
            loigiai_6 = ('Gọi biến cố $E:$"Mặt xuất hiện số chấm nhỏ hơn $%s$".\n'
                        'Ta có $E=%s$ nên $n(E)=%s$.'
                        %(latex(f),latex(f2),latex(f-1)))
            loigiai_7 = ('Gọi biến cố $F:$"Mặt xuất hiện số chấm không nhỏ hơn $%s$".\n'
                        'Ta có $F=%s$ nên $n(E)=%s$.'
                        %(latex(g),latex(g2),latex(7-g)))

            # Đưa các lời giải vào danh sách lời giải
            list_2 = [loigiai_1, loigiai_2, loigiai_3, loigiai_4, loigiai_5, loigiai_6, loigiai_7]

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

