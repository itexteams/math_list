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


def bt_dang5_p2_b1_c1_hh12(self):
            # Khai báo biến
            m=randint(1,9)
            a=randint(10,50)
            f=m*a

            # Nội dung câu hỏi
            noidungcauhoi = '''Theo định luật II Newton: Nếu $\\vec{F}$ là vectơ lực (N) tác dụng lên vật, $\\vec{a}$ là vectơ gia tốc của vật (m/s$^2$) và $m$ (kg) là khối lượng của vật thì ta có $\\vec{F}=m \\cdot \\vec{a}$. \n'''

            # Các đáp án
            da_1_d = '\\True Vectơ $\\vec{F}$ luôn cùng hướng với $\\vec{a}$'
            da_1_s = 'Vectơ $\\vec{F}$ luôn ngược hướng với $\\vec{a}$'
            list_da_1=[da_1_d,da_1_s]
            da_1=random.choice(list_da_1)

            da_2_d = '\\True Độ lớn của lực tác dụng lên vật luôn tỉ lệ thuận với độ lớn của gia tốc của vật'
            da_2_s = 'Độ lớn của lực tác dụng lên vật luôn tỉ lệ nghịch với độ lớn của gia tốc của vật'
            list_da_2=[da_2_d,da_2_s]
            da_2=random.choice(list_da_2)

            da_3_d = '\\True Muốn vật có khối lượng $%s$ kg chuyển động với gia tốc $%s$ (m/s$^2$) thì độ lớn lực cần tác dụng lên vật là $%s$ (N)' %(latex(m),latex(a),latex(m*a))
            da_3_s = 'Muốn vật có khối lượng $%s$ kg chuyển động với gia tốc $%s$ (m/s$^2$) thì độ lớn lực cần tác dụng lên vật là $%s$ (N)' %(latex(m),latex(a),latex(m*a+1))
            list_da_3=[da_3_d,da_3_s]
            da_3=random.choice(list_da_3)

            da_4_d = '\\True Lực có độ lớn $%s$ (N) tác dụng lên một vật làm vật rơi với gia tốc $%s$ (m/s$^2$). Khi đó khối lượng của vật là $%s$ (kg)'%(latex(f),latex(a),latex(m))
            da_4_s = 'Lực có độ lớn $%s$ (N) tác dụng lên một vật làm vật rơi với gia tốc $%s$ (m/s$^2$). Khi đó khối lượng của vật là $%s$ (kg)'%(latex(f),latex(a),latex(m+1))
            list_da_4=[da_4_d,da_4_s]
            da_4=random.choice(list_da_4)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_1, da_2, da_3, da_4]

            # Nội dung lời giải
            loigiai_1 = ('Vì $m>0$ nên vectơ $\\vec{F}$ luôn cùng hướng với $\\vec{a}$.'

                        )
            loigiai_2 = ('Ta có $\\vec{F}=m \\cdot \\vec{a}$ suy ra $\\left| \\vec{F} \\right|=m \\cdot \\left| \\vec{a} \\right|$ nên độ lớn của lực tác dụng lên vật luôn tỉ lệ thuận với độ lớn của gia tốc của vật.'
                        )
            loigiai_3 = ('Ta có $\\left| \\vec{F} \\right|=m \\cdot \\left| \\vec{a} \\right|=%s \\cdot %s=%s$ (N).'
                        %(latex(m),latex(a),latex(m*a)
                        ))
            loigiai_4 = ('$\\left| \\vec{F} \\right|=m \\cdot \\left| \\vec{a} \\right| \\Leftrightarrow m=\\dfrac{\\left| \\vec{F} \\right|}{\\left| \\vec{a} \\right|}=\\dfrac{%s}{%s}=%s$ (kq).'
                        %(latex(f),latex(a),latex(m)
                        ))

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
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions[0])+'\n'
                '\\item '+str(shuffled_solutions[1])+'\n'
                '\\item '+str(shuffled_solutions[2])+'\n'
                '\\item '+str(shuffled_solutions[3])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

