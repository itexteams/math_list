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


def bt_dang1_p3_b4_c1_ds11(self):
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random dữ liệu đầu vào
                a = randint(2, 5) # Giới hạn 2-5 để hình vẽ đẹp, không quá sát
                b = randint(2, 5)

                # Tính toán kết quả bài toán
                t = (Rational(1, a) + Rational(1, b)) / (1 - (Rational(1, a)) * (Rational(1, b)))
                goc = atan(t)
                h1 = goc * 180 / pi
                number = Decimal(float(h1))
                kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)


                pos_m_y = 4.0 / a
                pos_n_x = 4.0 / b

                # Làm tròn tọa độ để chuỗi TikZ gọn gàng
                pos_m_y_str = str(round(pos_m_y, 3))
                pos_n_x_str = str(round(pos_n_x, 3))

                # Nội dung câu hỏi
                # Lưu ý: Các placeholder %s trong TikZ sẽ nhận giá trị tọa độ đã tính ở trên
                noidungcauhoi = ('\\immini{ Trên một mảnh đất hình vuông $ABCD$, bác An đặt một chiếc đèn pin tại vị trí $A$ chiếu chùm sáng phân kỳ sang phía góc $C$. Bác An nhận thấy góc chiếu sáng của đèn pin giới hạn bởi hai tia $AM$ và $AN$, với các điểm $M, N$ lần lượt thuộc các cạnh $BC, CD$ sao cho $BM=%s BC, DN=%s DC$. Góc chiếu sáng của đèn pin bằng bao nhiêu độ (làm tròn kết quả đến phần nguyên của độ).'
                                 '}{'
                                 '\\scalebox{0.9}{ \n'
                                 '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                 '\\clip(-0.6,-0.6) rectangle (4.5,4.5); \n'
                                 '\\draw [line width=1.pt] (0.,0.)-- (4.,0.); \n' # AB
                                 '\\draw [line width=1.pt] (0.,0.)-- (0.,4.); \n' # AD
                                 '\\draw [line width=1.pt] (0.,4.)-- (4.,4.); \n' # DC
                                 '\\draw [line width=1.pt] (4.,4.)-- (4.,0.); \n' # BC
                                 '\\draw [line width=1.pt] (0.,0.)-- (%s,4.); \n' 
                                 '\\draw [line width=1.pt] (0.,0.)-- (4.,%s); \n' 
                                 '\\draw (-0.2,0.2) node[below] {$A$}; \n'
                                 '\\draw (4.0,-0.2) node[] {$B$}; \n'
                                 '\\draw (4.0,4.2) node[] {$C$}; \n'
                                 '\\draw (-0.2,4.2) node[] {$D$}; \n'
                                 '\\draw (%s,4.2) node[] {$N$}; \n' 
                                 '\\draw (4.2,%s) node[] {$M$}; \n' 
                                 '\\end{tikzpicture} } } \n'

                                 %(latex(Rational(1, a)), latex(Rational(1, b)),
                                   pos_n_x_str, pos_m_y_str,
                                   pos_n_x_str, pos_m_y_str
                                   ))

                # Nội dung lời giải
                loigiai = ('Trong tam giác vuông $ABM$ ta có $\\tan \\widehat{BAM}=\\dfrac{BM}{BA}=%s$. \\\\ \n'
                           'Trong tam giác vuông $ADN$ ta có $\\tan \\widehat{DAN}=\\dfrac{DN}{DA}=%s$. \\\\ \n'
                           'Do đó \\\\ \n'
                           '\\hspace*{1cm} $\\tan \\left( \\widehat{BAM}+\\widehat{DAN} \\right)=\\dfrac{\\tan \\widehat{BAM} +\\tan \\widehat{DAN} }{ 1-\\tan \\widehat{BAM} \\tan \\widehat{DAN} }=\\frac{%s+%s}{1-%s \\cdot %s}=%s$. \\\\ \n'
                           'Suy ra $\\widehat{BAM}+\\widehat{DAN} \\approx %s^\\circ$. \\\\ \n'
                           'Góc chiếu sáng của đèn pin bằng $90^\\circ-%s^\\circ=%s^\\circ$.'
                           % (latex(Rational(1, a)),
                              latex(Rational(1, b)),
                              latex(Rational(1, a)), latex(Rational(1, b)), latex(Rational(1, a)), latex(Rational(1, b)), latex(t),
                              latex(kq),
                              latex(kq), latex(90 - kq)
                              ))

                # Đáp án
                dapan = ' \\shortans[0]{$%s$} ' % (latex(90 - kq))

            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
                       '\\loigiai{ \n'
                       + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

