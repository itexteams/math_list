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


def bt_dang2_p2_b1_c6_ds10(self):
            # Khai báo biến
            a = randint(4,6)
            b = randint(2,6)
            if b==2:
                b = randint(2,6)
            c = randint(2,6)
            if c==3:
                c = randint(2,6)
            d = randint(2,6)
            if d==6:
                d = randint(2,6)
            e = randint(2,6)
            if e==2:
                e = randint(2,6)
            f = randint(2,6)
            if f==2:
                f = randint(2,6)
            g=randint(3,6)
            if g==3:
                f1 = randint(4,6)
            # Nội dung câu hỏi
            noidungcauhoi = '''Gieo một con xúc xắc cân đối và đồng chất một lần.'''

            # Các đáp án
            da_1_d = '\\True Xác suất xuất hiện số lớn hơn $2$ là $\\mathrm{P}(H)=\\dfrac{2}{3}$'
            da_1_s = 'Xác suất xuất hiện số lớn hơn $4$ là $\\mathrm{P}(H)=\\dfrac{2}{%s}$' %(latex(a))
            list_da_1=[da_1_d,da_1_s]
            da_1=random.choice(list_da_1)

            da_2_d = '\\True Xác suất mặt lẻ chấm xuất hiện là $\\mathrm{P}(A)=\\dfrac{1}{2}$'
            da_2_s = 'Xác suất mặt lẻ chấm xuất hiện là $\\mathrm{P}(A)=\\dfrac{1}{%s}$'%(latex(b))
            list_da_2=[da_2_d,da_2_s]
            da_2=random.choice(list_da_2)

            da_3_d = '\\True Xác suất xuất hiện số chấm chia hết cho $3$ là $\\mathrm{P}(B)=\\dfrac{1}{3}$'
            da_3_s = 'Xác suất xuất hiện số chấm chia hết cho $3$ là $\\mathrm{P}(B)=\\dfrac{1}{%s}$'%(latex(c))
            list_da_3=[da_3_d,da_3_s]
            da_3=random.choice(list_da_3)

            da_4_d = '\\True Xác suất xuất hiện số chấm chia hết cho $5$ là $\\mathrm{P}(C)=\\dfrac{1}{6}$'
            da_4_s = 'Xác suất xuất hiện số chấm chia hết cho $5$ là $\\mathrm{P}(C)=\\dfrac{1}{%s}$'%(latex(d))
            list_da_4=[da_4_d,da_4_s]
            da_4=random.choice(list_da_4)

            da_5_d = '\\True Xác suất xuất hiện số chấm là số nguyên tố $\\mathrm{P}(D)=\\dfrac{1}{2}$'
            da_5_s = 'Xác suất xuất hiện số chấm là số nguyên tố $\\mathrm{P}(D)=\\dfrac{1}{%s}$' %(latex(e))
            list_da_5=[da_5_d,da_5_s]
            da_5=random.choice(list_da_5)

            da_6_d = '\\True Xác suất xuất hiện số chấm nhỏ hơn $3$ là $\\mathrm{P}(E)=\\dfrac{1}{3}$'
            da_6_s = 'Xác suất xuất hiện số chấm nhỏ hơn $3$ là $\\mathrm{P}(E)=\\dfrac{1}{%s}$'%(latex(f))
            list_da_6=[da_6_d,da_6_s]
            da_6=random.choice(list_da_6)

            da_7_d = '\\True Xác suất xuất hiện số không lớn hơn $4$ là $\\mathrm{P}(F)=\\dfrac{2}{3}$'
            da_7_s = 'Xác suất xuất hiện số không lớn hơn $4$ là $\\mathrm{P}(F)=\\dfrac{2}{%s}$' %(latex(g))
            list_da_7=[da_7_d,da_7_s]
            da_7=random.choice(list_da_7)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_1, da_2, da_3, da_4, da_5, da_6, da_7]

            # Nội dung lời giải
            loigiai_1 = ('Ta có $\\Omega=\\left\\{ 1;2;3;4;5;6 \\right\\}\\Rightarrow n(\\Omega)=6$. \n'
                        'Gọi biến cố $H:$"Mặt xuất hiện số chấm lớn hơn $2$".\n'
                        'Khi đó $H= \\left \\lbrace 3;4;5;6 \\right \\rbrace$ nên $n(F)=4$.\n'
                        'Vậy $\\mathrm{P}(H)=\\dfrac{n(H)}{n(\\Omega)}=\\dfrac{4}{6}=\\dfrac{2}{3}$.')
            loigiai_2 = ('Ta có $\\Omega=\\left\\{ 1;2;3;4;5;6 \\right\\}\\Rightarrow n(\\Omega)=6$.\n'
                        'Gọi biến cố $A:$"Mặt xuất hiện số chấm lẻ".\n'
                        'Ta có $A=\\left \\lbrace 1;3;5 \\right \\rbrace$ nên $n(A)=3$.\n'
                        'Vậy $\\mathrm{P}(A)=\\dfrac{n(A)}{n(\\Omega)}=\\dfrac{3}{6}=\\dfrac{1}{2}$.')
            loigiai_3 = ('Ta có $\\Omega=\\left\\{ 1;2;3;4;5;6 \\right\\}\\Rightarrow n(\\Omega)=6$.\n'
                        'Gọi biến cố $B:$"Mặt xuất hiện số chấm chia hết cho $3$".\n'
                        'Khi đó $B= \\left \\lbrace 3;6 \\right \\rbrace$ nên $n(B)=2$.\n'
                        'Vậy $\\mathrm{P}(B)=\\dfrac{n(B)}{n(\\Omega)}=\\dfrac{2}{6}=\\dfrac{1}{3}$.')
            loigiai_4 = ('Ta có $\\Omega=\\left\\{ 1;2;3;4;5;6 \\right\\}\\Rightarrow n(\\Omega)=6$. \n'
                        'Gọi biến cố $C:$"Mặt xuất hiện số chấm chia hết cho $5$".\n'
                        'Khi đó $C= \\left \\lbrace 5 \\right \\rbrace$ nên $n(C)=1$.\n'
                        'Vậy $\\mathrm{P}(C)=\\dfrac{n(C)}{n(\\Omega)}=\\dfrac{1}{6}$.')
            loigiai_5 = ('Ta có $\\Omega=\\left\\{ 1;2;3;4;5;6 \\right\\}\\Rightarrow n(\\Omega)=6$.\n'
                        'Gọi biến cố $D:$"Mặt xuất hiện số chấm là số nguyên tố". \n'
                        'Khi đó $D= \\left \\lbrace 2;3;5 \\right \\rbrace$ nên $n(D)=3$.\n'
                        'Vậy $\\mathrm{P}(D)=\\dfrac{n(D)}{n(\\Omega)}=\\dfrac{3}{6}=\\dfrac{1}{2}$.')
            loigiai_6 = ('Ta có $\\Omega=\\left\\{ 1;2;3;4;5;6 \\right\\}\\Rightarrow n(\\Omega)=6$.\n'
                        'Gọi biến cố $E:$"Mặt xuất hiện số chấm nhỏ hơn $3$".\n'
                        'Khi đó $E= \\left \\lbrace 1;2 \\right \\rbrace$ nên $n(E)=2$.\n'
                        'Vậy $\\mathrm{P}(E)=\\dfrac{n(E)}{n(\\Omega)}=\\dfrac{2}{6}=\\dfrac{1}{3}$.')
            loigiai_7 = ('Ta có $\\Omega=\\left\\{ 1;2;3;4;5;6 \\right\\}\\Rightarrow n(\\Omega)=6$.\n'
                        'Gọi biến cố $F:$"Mặt xuất hiện số chấm không lớn hơn $4$". \n'
                        'Khi đó $F= \\left \\lbrace 1;2;3;4 \\right \\rbrace$ nên $n(F)=4$.\n'
                        'Vậy $\\mathrm{P}(F)=\\dfrac{n(F)}{n(\\Omega)}=\\dfrac{4}{6}=\\dfrac{2}{3}$.')
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

