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


def bt_dang1_p2_b2_c6_ds10(self):
            # Khai báo biến
            a = randint(6,9)
            b = randint(2,4)
            c = randint(2,9)
            d = randint(2,5)
            xa=math.comb(20,a)
            x1= math.comb(8,d)
            x11= math.comb(12,a-d)
            x1d=Rational(x1*x11,xa)#Xác suất Lấy d số nguyên tố
            x1s=Rational(x1*x11+2,xa)#Xác suất Lấy d số nguyên tố
            xb = math.comb(10,a) # Số pt biến cố lấy a số chẵn da1
            x2d=Rational(xb,xa)#Xác suất Lấy a số chẵn
            x2s=Rational(xb+10,xa)
            xc=math.comb(10,b) #số phần tử lấy b số chẵn da2
            xl = math.comb(10,a-b) # Số pt biến cố lấy b1 số lẻ
            x3d=Rational(xc*xl,xa)#Xác suất Lấy a số chẵn b1 số lẻ
            x3s=Rational(xc*xl-10,xa)
            j=set()
            for i in range(2, 20+1):
                if i % c == 0:
                    j.add(i)
            x4=len(set(j))
            x4a=math.comb(20-x4,a) # số phần tử bc B ngang
            x4d=1-Rational(x4a,xa)
            x4s=1-Rational(x4a+10,xa)

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
            noidungcauhoi = '''Có $20$ tấm thẻ được đánh số từ $1$ đến $20$. Lấy ngẫu nhiên $%s$ thẻ.'''%(latex(a))

            # Các đáp án
            da_1_d = '\\True Xác suất để $%s$ thẻ lấy ra có $%s$ thẻ là số nguyên tố là $%s$' %(latex(a),latex(d),latex(x1d))
            da_1_s = 'Xác suất để $%s$ thẻ lấy ra có $%s$ thẻ là số nguyên tố là $%s$' %(latex(a),latex(d),latex(x1s))
            list_da_1=[da_1_d,da_1_s]
            da_1=random.choice(list_da_1)

            da_2_d = '\\True Xác suất để $%s$ thẻ lấy ra đều mang số chẵn là $%s$'%(latex(a),latex(x2d))
            da_2_s = 'Xác suất để $%s$ thẻ lấy ra đều mang số chẵn là $%s$'%(latex(a),latex(x2s))
            list_da_2=[da_2_d,da_2_s]
            da_2=random.choice(list_da_2)

            da_3_d = '\\True Xác suất để $%s$ thẻ lấy ra có $%s$ thẻ mang số chẵn và $%s$ thẻ mang số lẻ là $%s$'%(latex(a),latex(b),latex(a-b),latex(x3d))
            da_3_s = 'Xác suất để $%s$ thẻ lấy ra có $%s$ thẻ mang số chẵn và $%s$ thẻ mang số lẻ là $%s$'%(latex(a),latex(b),latex(a-b),latex(x3s))
            list_da_3=[da_3_d,da_3_s]
            da_3=random.choice(list_da_3)

            da_4_d = '\\True Xác suất để có ít nhất một số ghi trên thẻ được chọn chia hết cho $%s$ là $%s$'%(latex(c),latex(x4d))
            da_4_s = 'Xác suất để có ít nhất một số ghi trên thẻ được chọn chia hết cho $%s$ là $%s$'%(latex(c),latex(x4s))
            list_da_4=[da_4_d,da_4_s]
            da_4=random.choice(list_da_4)
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_1, da_2, da_3, da_4]

            # Nội dung lời giải
            loigiai_1 =( 'Gọi biến cố B: "$%s$ thẻ lấy ra có $%s$ thẻ ghi số nguyên tố".\\\\ \n'
                        'Từ $1$ đến $20$ có $8$ số nguyên tố. Khi đó $n(B)=\\mathrm{C}_{8}^{%s}\\cdot\\mathrm{C}_{12}^{%s}=%s$.\\\\ \n'
                        'Vậy $\\mathrm{P}(B)=\\dfrac{n(B)}{n(\\Omega)}=\\dfrac{%s}{%s}=%s$.'
                        %(latex(a),latex(d),
                            latex(d),latex(a-d),latex(x1*x11),
                            latex(x1*x11),latex(xa),latex(x1d)))
            loigiai_2 = ('Gọi biến cố A: "$%s$ thẻ lấy ra đều là số chẵn".\\\\ \n'
                        'Từ $1$ đến $20$ có $10$ số chẵn. Khi đó $n(A)=\\mathrm{C}_{10}^{%s}=%s$.\\\\ \n'
                        'Vậy $\\mathrm{P}(A)=\\dfrac{n(A)}{n(\\Omega)}=\\dfrac{%s}{%s}=%s$.'
                        %(latex(a),
                            latex(a),latex(xb),
                            latex(xb),latex(xa),latex(x2d)))
            loigiai_3 = ('Gọi biến cố C: "$%s$ thẻ lấy ra có $%s$ thẻ mang số chẵn và $%s$ thẻ mang số lẻ".\\\\ \n'
                        'Từ $1$ đến $20$ có $10$ số chẵn và $10$ số lẻ. Khi đó $n(C)=\\mathrm{C}_{10}^{%s}\\cdot\\mathrm{C}_{10}^{%s}=%s$.\\\\ \n'
                        'Vậy $\\mathrm{P}(C)=\\dfrac{n(C)}{n(\\Omega)}=\\dfrac{%s}{%s}=%s$.'
                        %(latex(a),latex(b),latex(a-b),
                            latex(b),latex(a-b),latex(xc*xl),
                            latex(xc*xl),latex(xa),latex(x3d)))
            loigiai_4 = ( 'Gọi biến cố D: "$%s$ thẻ lấy ra có ít nhất một thẻ có số chia hết cho $%s$".\\\\ \n'
                        'Khi đó $\\overline{D}$: "$%s$ thẻ lấy ra không có thẻ có số chia hết cho $%s$".\\\\ \n'
                        'Từ $1$ đến $20$ có $%s$ số không chia hết cho $%s$. Khi đó $n(\\overline{D})=\\mathrm{C}_{%s}^{%s}=%s$.\\\\ \n'
                        'Vậy $\\mathrm{P}(D)=1-\\mathrm{P}(\\overline{D})=1-\\dfrac{%s}{%s}=%s$.'
                        %(latex(a),latex(c),
                            latex(a),latex(c),
                            latex(20-x4),latex(c),latex(20-x4),latex(a),latex(x4a),
                            latex(x4a),latex(xa),latex(x4d)))

            # Đưa các lời giải vào danh sách lời giải
            list_2 = [loigiai_1, loigiai_2, loigiai_3, loigiai_4]

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
                'Số phần tử của không gian mẫu là $n(\\Omega)=\\mathrm{C}_{20}^{'+latex(a)+'}='+latex(xa)+'$. \\\\ \n' 
                '\\begin{enumEX}[a)]{1} \n' 
                '\\item '+str(shuffled_solutions[0])+'\n'
                '\\item '+str(shuffled_solutions[1])+'\n'
                '\\item '+str(shuffled_solutions[2])+'\n'
                '\\item '+str(shuffled_solutions[3])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n' ).replace('--','').replace('\\frac','\\dfrac').replace('+-','-').replace('++','+')
            return content

