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


def bt_dang2_p3_b1_c1_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                t=symbols('t')

                a=randint(-9,-1)
                b=randint(1,50)
                while b%(2*a)!=0:
                    a=randint(-9,-1)
                    b=randint(1,50)

                t0=-Rational(b,2*a)

                # --- XỬ LÝ ĐỂ v(t) LUÔN DƯƠNG TRÊN [0, t0+10] ---
                # Tính giá trị của phần (at^2 + bt) tại t = t0 + 10
                val_at_tend = a * (t0 + 10)**2 + b * (t0 + 10)

                # c phải lớn hơn 0 VÀ lớn hơn -val_at_tend để v(t0+10) > 0
                min_c = max(1, -int(val_at_tend) + 1)

                # Random c từ giá trị tối thiểu để đảm bảo yêu cầu (cộng thêm khoảng ngẫu nhiên để bài toán đa dạng)
                c = randint(min_c, min_c + 30) 

                d=randint(-9,9)
                # ------------------------------------------------

                v=a*t**2+b*t+c
                daoham=2*a*t+b
                s=Rational(a,3)*t**3+Rational(b,2)*t**2+c*t+d

                # Nội dung câu hỏi
                noidungcauhoi = ('Một vật chuyển động theo quy luật $s(t)=%s$ với $t$ (giây) là khoảng thời gian từ lúc bắt đầu chuyển động và $s(t)$ (m) là quãng đường vật đi được trong khoảng thời gian đó. Hỏi trong khoảng $%s$ giây kể từ lúc bắt đầu chuyển động, vật chuyển động chậm dần sau giây thứ bao nhiêu? \n'
                                %(latex(s),latex(t0+10)
                                ))

                # Nội dung lời giải
                loigiai = ('Vận tốc của vật được xác định theo công thức $v(t)=%s$. \\\\ \n'
                        'Ta có $v\'(t)=%s$; $v\'(t)=0 \\Leftrightarrow t=%s$. \\\\ \n'
                        'Bảng biến thiên \\\\ \n'
                        '\\hspace*{1cm} \\begin{tikzpicture}    \n'
                        '\\tkzTabInit[espcl=2.5,lgt=1.5]  \n'
                            '{$t$/0.7,$v\'(t)$/0.7,$v(t)$/2.1} \n'
                        ' {$0$,$%s$,$%s$}  \n'
                            '\\tkzTabLine{,+,0,-,} \n'
                            '\\tkzTabVar{-/,+/,-/}  \n'
                        '\\end{tikzpicture}   \\\\ \n'
                        'Từ bảng biến thiên ta thấy \\\\ \n'
                        '\\hspace*{1cm} Từ thời điểm bắt đầu chuyển động đến thời điểm $t=%s$ giây, vật chuyển động nhanh dần. \\\\ \n'
                        '\\hspace*{1cm} Từ sau thời điểm $t=%s$ giây, vật chuyển động chậm dần. \\\\ \n'
                        'Vậy vật chuyển động chậm dần sau giây thứ $%s$. \\\\ \n'
                        %(latex(v),
                            latex(daoham),latex(t0),
                            latex(t0),latex(t0+10),
                            latex(t0),latex(t0),latex(t0)
                            ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(t0))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content              

