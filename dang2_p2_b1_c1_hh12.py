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


def bt_dang2_p2_b1_c1_hh12(self):
            # Khai báo biến

            # Nội dung câu hỏi
            noidungcauhoi = '''Cho hình lăng trụ $ABC.A\'B\'C\'$. Gọi $M$ là trung điểm của $BB\'$ và $G$ là trọng tâm của tam giác $ABC$. \n'''

            # Các đáp án
            da_1_d = '\\True $\\overrightarrow{BM}=\\dfrac{1}{2} \\overrightarrow{BB\'}$'
            da_1_s = '$\\overrightarrow{BM}=\\dfrac{1}{3} \\overrightarrow{BB\'}$'
            list_da_1=[da_1_d,da_1_s]
            da_1=random.choice(list_da_1)

            da_2_d = '\\True $\\overrightarrow{AM}=\\overrightarrow{AB}+\\dfrac{1}{2} \\overrightarrow{BB\'}$'
            da_2_s = '$\\overrightarrow{AM}=\\overrightarrow{AB}-\\dfrac{1}{2} \\overrightarrow{BB\'}$'
            list_da_2=[da_2_d,da_2_s]
            da_2=random.choice(list_da_2)

            da_3_d = '\\True $\\overrightarrow{AM}=\\dfrac{1}{2} \\overrightarrow{AB}+\\dfrac{1}{2} \\overrightarrow{AB\'}$'
            da_3_s = '$\\overrightarrow{AM}=\\overrightarrow{AB}+\\overrightarrow{AB\'}$'
            list_da_3=[da_3_d,da_3_s]
            da_3=random.choice(list_da_3)

            da_4_d = '\\True $\\overrightarrow{GA}+\\overrightarrow{GB}+\\overrightarrow{GC}=\\overrightarrow{0}$'
            da_4_s = '$\\overrightarrow{GA}+\\overrightarrow{GB}+\\overrightarrow{GC}=\\overrightarrow{AB}$'
            list_da_4=[da_4_d,da_4_s]
            da_4=random.choice(list_da_4)

            da_5_d = '\\True $\\overrightarrow{MA}+\\overrightarrow{MB}+\\overrightarrow{MC}=3 \\overrightarrow{MG}$'
            da_5_s = '$\\overrightarrow{MA}+\\overrightarrow{MB}+\\overrightarrow{MC}=-3 \\overrightarrow{MG}$'
            list_da_5=[da_5_d,da_5_s]
            da_5=random.choice(list_da_5)

            da_6_d = '\\True $\\overrightarrow{MG}-\\overrightarrow{MC}=\\overrightarrow{CG}$'
            da_6_s = '$\\overrightarrow{MG}-\\overrightarrow{MC}=\\overrightarrow{GC}$'
            list_da_6=[da_6_d,da_6_s]
            da_6=random.choice(list_da_6)

            da_7_d = '\\True Ba vectơ $\\overrightarrow{AA\'}, \\overrightarrow{BB\'}$ và $\\overrightarrow{CC\'}$ cùng phương'
            da_7_s = 'Ba vectơ $\\overrightarrow{AA\'}, \\overrightarrow{B\'B}$ và $\\overrightarrow{CC\'}$ cùng hướng'
            list_da_7=[da_7_d,da_7_s]
            da_7=random.choice(list_da_7)

            da_8_d = '\\True Ba vectơ $\\overrightarrow{AM}, \\overrightarrow{BB\'}$ và $\\overrightarrow{AB\'}$ đồng phẳng'
            da_8_s = 'Ba vectơ $\\overrightarrow{AM}, \\overrightarrow{BB\'}$ và $\\overrightarrow{AB\'}$ không đồng phẳng'
            list_da_8=[da_8_d,da_8_s]
            da_8=random.choice(list_da_8)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_1, da_2, da_3, da_4, da_5, da_6, da_7, da_8]

            # Nội dung lời giải
            loigiai_1 = ('$M$ là trung điểm của $BB\'$ nên $\\overrightarrow{BM}=\\dfrac{1}{2} \\overrightarrow{BB\'}$.'

                        )
            loigiai_2 = ('$M$ là trung điểm của $BB\'$ nên $\\overrightarrow{BM}=\\dfrac{1}{2} \\overrightarrow{BB\'}$.\\\\ \n'
                        'Ta có $\\overrightarrow{AM}=\\overrightarrow{AB}+\\overrightarrow{BM}=\\overrightarrow{AB}+\\dfrac{1}{2} \\overrightarrow{BB\'}$.'

                        )
            loigiai_3 = ('Theo quy tắc hình bình hành ta có $\\overrightarrow{AM}=\\dfrac{1}{2} \\overrightarrow{AB}+\\dfrac{1}{2} \\overrightarrow{AB\'}$.'

                        )
            loigiai_4 = ('Theo tính chất trọng tâm của tam giác ta có $\\overrightarrow{GA}+\\overrightarrow{GB}+\\overrightarrow{GC}=\\overrightarrow{0}$.'

                        )
            loigiai_5 = ('Ta có $\\overrightarrow{GA}+\\overrightarrow{GB}+\\overrightarrow{GC}=\\overrightarrow{0}$\\\\ \n'
                        '$\\Leftrightarrow  \\overrightarrow{GM}+\\overrightarrow{GA}+\\overrightarrow{GM}+\\overrightarrow{GB}+\\overrightarrow{GM}+\\overrightarrow{GC}=\\overrightarrow{0}$ \\\\ \n'
                        '$\\Leftrightarrow  3 \\overrightarrow{GM}+\\overrightarrow{GA}+\\overrightarrow{GB}+\\overrightarrow{GC}=\\overrightarrow{0}$ \\\\ \n'
                        '$\\Leftrightarrow \\overrightarrow{MA}+\\overrightarrow{MB}+\\overrightarrow{MC}=3 \\overrightarrow{MG}$.'

                        )
            loigiai_6 = ('Theo quy tắc trừ hai vectơ ta có $\\overrightarrow{MG}-\\overrightarrow{MC}=\\overrightarrow{CG}$.'

                        )
            loigiai_7 = ('Ba đường thẳng $AA\', BB\', CC\'$ đôi một song song nên ba vectơ $\\overrightarrow{AA\'}, \\overrightarrow{BB\'}$ và $\\overrightarrow{CC\'}$ cùng phương.'

                        )

            loigiai_8 = ('Vì $AM, BB\'$ và $AB\'$ cùng nằm trên mặt phẳng $(ABB\'A\')$ nên Ba vectơ $\\overrightarrow{AM}, \\overrightarrow{BB\'}$ và $\\overrightarrow{AB\'}$ đồng phẳng.'

                        )

            # Đưa các lời giải vào danh sách lời giải
            list_2 = [loigiai_1, loigiai_2, loigiai_3, loigiai_4, loigiai_5, loigiai_6, loigiai_7, loigiai_8]

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

                '\\begin{center}  \n'
                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]   \n'
                '\\clip(-0.7197428742153014,-1.6612826693767568) rectangle (4.546290529312646,3.8566045056242655); \n'
                '\\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (3.,0.); \n'
                '\\draw (0.,0.)-- (1.,-1.); \n'
                '\\draw (1.,-1.)-- (3.,0.); \n'
                '\\draw (0.,0.)-- (1.,3.); \n'
                '\\draw (1.,3.)-- (4.,3.); \n'
                '\\draw (4.,3.)-- (3.,0.); \n'
                '\\draw (1.,3.)-- (2.,2.); \n'
                '\\draw (2.,2.)-- (4.,3.); \n'
                '\\draw (2.,2.)-- (1.,-1.); \n'
                '\\draw (0.6425570714799719,3.5131675445246167) node[anchor=north west] {$A$}; \n'
                '\\draw (1.8,2.1) node[anchor=north west] {$B$}; \n'
                '\\draw (-0.6,0.2276206166713109) node[anchor=north west] {$A\'$}; \n'
                '\\draw (4.07692668247646,3.4902717471179736) node[anchor=north west] {$C$}; \n'
                '\\draw (0.7684839572165097,-0.9744087471774595) node[anchor=north west] {$B\'$}; \n'
                '\\draw (1.5011494742290938,0.7771197544307488) node[anchor=north west] {$M$}; \n'
                '\\draw (1.4614973901238113,2.538502609876189)-- (4.,3.); \n'
                '\\draw (1.,3.)-- (2.989619590226296,2.494809795113148); \n'
                '\\draw (1.,3.)-- (1.506171287172316,0.5185138615169482); \n'
                '\\draw (2.03920071328521,2.7) node[anchor=north west] {$G$}; \n'
                '\\draw (2.989376305660905,0.2276206166713109) node[anchor=north west] {$C\'$}; \n'
                '\\end{tikzpicture} \n'
                '\\end{center} \n'

                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions[0])+'\n'
                '\\item '+str(shuffled_solutions[1])+'\n'
                '\\item '+str(shuffled_solutions[2])+'\n'
                '\\item '+str(shuffled_solutions[3])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

