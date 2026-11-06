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


def bt_dang3_p2_b1_c1_hh12(self):
            # Khai báo biến
            a=randint(1,9)
            # Nội dung câu hỏi
            noidungcauhoi = '''Cho hình chóp tứ giác đều $S.ABCD$, đáy có tâm $O$ và cạnh bằng $%s$, cạnh bên bằng $%s$. $M$ là trung điểm của $AB$. \n'''%(latex(a),latex(2*a))

            # Các đáp án
            da_1_d = '\\True Góc giữa hai vectơ $\\overrightarrow{AD}$ và $\\overrightarrow{CB}$ bằng $180^\\circ$'
            da_1_s = 'Góc giữa hai vectơ $\\overrightarrow{AD}$ và $\\overrightarrow{CB}$ bằng $0^\\circ$'
            list_da_1=[da_1_d,da_1_s]
            da_1=random.choice(list_da_1)

            da_2_d = '\\True Độ dài vectơ $\\overrightarrow{BD}$ bằng $%s$' %(latex(a*sqrt(2)))
            da_2_s = 'Độ dài vectơ $\\overrightarrow{BD}$ bằng $%s$' %(latex(a))
            list_da_2=[da_2_d,da_2_s]
            da_2=random.choice(list_da_2)

            da_3_d = '\\True $\\left| \\overrightarrow{SA}+\\overrightarrow{SB} \\right|=%s$'%(latex(a*sqrt(15)))
            da_3_s = '$\\left| \\overrightarrow{SA}+\\overrightarrow{SB} \\right|=%s$'%(latex((a*sqrt(15))/2))
            list_da_3=[da_3_d,da_3_s]
            da_3=random.choice(list_da_3)

            da_4_d = '\\True Cosin của góc giữa hai vectơ $\\overrightarrow{CD}$ và $\\overrightarrow{BS}$ bằng $\\dfrac{1}{4}$'
            da_4_s = 'Cosin của góc giữa hai vectơ $\\overrightarrow{CD}$ và $\\overrightarrow{BS}$ bằng $\\dfrac{1}{2}$'
            list_da_4=[da_4_d,da_4_s]
            da_4=random.choice(list_da_4)

            da_5_d = '\\True Góc giữa hai vectơ $\\overrightarrow{AO}$ và $\\overrightarrow{SD}$ bằng $90^\\circ$'
            da_5_s = 'Góc giữa hai vectơ $\\overrightarrow{AO}$ và $\\overrightarrow{SD}$ bằng $60^\\circ$'
            list_da_5=[da_5_d,da_5_s]
            da_5=random.choice(list_da_5)

            da_6_d = '\\True $\\overrightarrow{SB}+\\overrightarrow{SD}=2 \\overrightarrow{SO}$'
            da_6_s = '$\\overrightarrow{SB}+\\overrightarrow{SD}=\\overrightarrow{SO}$'
            list_da_6=[da_6_d,da_6_s]
            da_6=random.choice(list_da_6)

            da_7_d = '\\True Hai vectơ $\\overrightarrow{BC}$ và $\\overrightarrow{DA}$ đối nhau'
            da_7_s = 'Hai vectơ $\\overrightarrow{BC}$ và $\\overrightarrow{DA}$ bằng nhau'
            list_da_7=[da_7_d,da_7_s]
            da_7=random.choice(list_da_7)

            da_8_d = '\\True $\\left| \\overrightarrow{SC}+\\overrightarrow{CO} \\right|=%s$' %(latex((a*sqrt(14))/2))
            da_8_s = '$\\left| \\overrightarrow{SC}+\\overrightarrow{CO} \\right|=%s$' %(latex((a*sqrt(14))/3))
            list_da_8=[da_8_d,da_8_s]
            da_8=random.choice(list_da_8)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_1, da_2, da_3, da_4, da_5, da_6, da_7, da_8]

            # Nội dung lời giải
            loigiai_1 = ('Hai vectơ $\\overrightarrow{AD}$ và $\\overrightarrow{CB}$ ngược hướng nên góc giữa hai vectơ bằng $180^\\circ$.'

                        )
            loigiai_2 = ('Ta có $BD$ là đường chéo của hình vuông nên $BD=%s$.\\\\ \n'
                        'Vậy độ dài vectơ $\\overrightarrow{BD}$ bằng $%s$.'
                        %(latex(a*sqrt(2)),latex(a*sqrt(2)))
                        )
            loigiai_3 = ('Ta có \\\\ \n'
                        '$SM=\\sqrt{SA^2-MA^2}=%s$. \\\\ \n'
                        'Suy ra $\\left| \\overrightarrow{SA}+\\overrightarrow{SB} \\right|=2 \\left| \\overrightarrow{AM} \\right|=%s$.'
                        %(latex((a*sqrt(15))/2),latex((a*sqrt(15)))
                        ))
            loigiai_4 = ('Ta có $\\left( \\overrightarrow{CD}, \\overrightarrow{BS} \\right) =\\left( \\overrightarrow{BA}, \\overrightarrow{BS} \\right)$.\\\\ \n'
                        'Xét tam giác $SBM$ ta có $\\cos B=\\dfrac{BM}{BS}=\\dfrac{1}{4}$. \\\\ \n'
                        'Vậy cosin của góc giữa hai vectơ $\\overrightarrow{CD}$ và $\\overrightarrow{BS}$ bằng $\\dfrac{1}{4}$.'

                        )
            loigiai_5 = ('Vì $AO$ vuông góc với $SD$ nên $\\left( \\overrightarrow{AO}, \\overrightarrow{SD} \\right)=90^\\circ$.'

                        )
            loigiai_6 = ('Theo quy tắc hình bình hành ta có $\\overrightarrow{SB}+\\overrightarrow{SD}=2 \\overrightarrow{SO}$.'

                        )
            loigiai_7 = ('Hai vectơ $\\overrightarrow{BC}$ và $\\overrightarrow{DA}$ ngược hướng và có độ dài bằng nhau nên đối nhau.'

                        )

            loigiai_8 = ('Xét tam giác $SOC$, ta có \\\\ \n'
                        '$SO=\\sqrt{SC^2-CO^2}=%s$. \\\\ \n'
                        'Do đó $\\left| \\overrightarrow{SC}+\\overrightarrow{CO} \\right|=\\left| \\overrightarrow{SO} \\right|=SO=%s$.'
                        %(latex((a*sqrt(14))/2),latex((a*sqrt(14))/2)
                        ))

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
                '\\clip(-0.809906902845595,-0.683575353673238) rectangle (5.188413574762594,4.605164625795179); \n'
                '\\draw (0.,0.)-- (3.,0.); \n'
                '\\draw (3.,0.)-- (4.5,1.5); \n'
                '\\draw [dash pattern=on 2pt off 2pt] (4.5,1.5)-- (1.5,1.5); \n'
                '\\draw [dash pattern=on 2pt off 2pt] (1.5,1.5)-- (0.,0.); \n'
                '\\draw [dash pattern=on 2pt off 2pt] (1.5,1.5)-- (3.,0.); \n'
                '\\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (4.5,1.5); \n'
                '\\draw [dash pattern=on 2pt off 2pt] (2.25,0.75)-- (2.283864069043802,4.009117007357772); \n'
                '\\draw [dash pattern=on 2pt off 2pt] (2.283864069043802,4.009117007357772)-- (1.5,1.5); \n'
                '\\draw (2.283864069043802,4.009117007357772)-- (0.,0.); \n'
                '\\draw (2.283864069043802,4.009117007357772)-- (4.5,1.5); \n'
                '\\draw (2.283864069043802,4.009117007357772)-- (3.,0.); \n'
                '\\draw (2.283864069043802,4.009117007357772)-- (1.4891339111272597,0.); \n'
                '\\draw (2,4.55) node[anchor=north west] {$S$}; \n'
                '\\draw (-0.5,0.18684339071154624) node[anchor=north west] {$A$}; \n'
                '\\draw (2.9745224205665113,0.054388364392122565) node[anchor=north west] {$B$}; \n'
                '\\draw (4.554521663091066,1.8236090730872816) node[anchor=north west] {$C$}; \n'
                '\\draw (0.9,1.8898365862469935) node[anchor=north west] {$D$}; \n'
                '\\draw (1.8,0.8112742290745436) node[anchor=north west] {$O$}; \n'
                '\\draw (1.2431460051054728,0.06384943770065282) node[anchor=north west] {$M$}; \n'
                '\\end{tikzpicture} \n'
                '\\end{center}  \n'

                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions[0])+'\n'
                '\\item '+str(shuffled_solutions[1])+'\n'
                '\\item '+str(shuffled_solutions[2])+'\n'
                '\\item '+str(shuffled_solutions[3])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

