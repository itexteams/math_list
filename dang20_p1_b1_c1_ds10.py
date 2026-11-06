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


def bt_dang20_p1_b1_c1_ds10(self):
    # Khai báo biến
    lisdang = ['1','2','3','4','5','6','7','8','9'] # Đã điều chỉnh theo dữ liệu thực tế
    dang = random.choice(lisdang)

    if dang == '1':
        du = ['$P(1)$ chia hết cho 3']
        da = random.choice(du)
        s = ['$P(6)$ chia hết cho 5', '$P(8)$ không chia hết cho 3', '$P(11)$ không chia hết cho 2', '$P(12)$ chia hết cho 10', '$P(5)$ không chia hết cho 8', '$P(2)$ không chia hết cho 3', ' $P(9)$ không chia hết cho 4', '$P(4)$ chia hết cho 4', '$P(10)$ chia hết cho 10', '$P(3)$ không chia hết cho 8', '$P(7)$ chia hết cho 5']
        das1 = random.choice(s); s.remove(das1)
        das2 = random.choice(s); s.remove(das2)
        das3 = random.choice(s)
        noidungcauhoi = 'Cho mệnh đề chứa biến $P(n)=n^2-1$. Mệnh đề nào sau đây là đúng?. \n'
        da_d = '\\True ' + str(da)
        da_s1, da_s2, da_s3 = str(das1), str(das2), str(das3)
        loigiai = '$P(1)=1^2-1=0$ nên chia hết cho 3.'

    elif dang == '2':
        du = ['$P(2)$ chia hết cho 3']
        da = random.choice(du)
        s = ['$P(1)$ không chia hết cho 3', '$P(6)$ chia hết cho 5', '$P(8)$ không chia hết cho 3', '$P(11)$ không chia hết cho 2', '$P(12)$ chia hết cho 10', '$P(5)$ không chia hết cho 8', ' $P(9)$ không chia hết cho 4', '$P(4)$ chia hết cho 4', '$P(10)$ chia hết cho 10', '$P(3)$ không chia hết cho 8', '$P(7)$ chia hết cho 5']
        das1 = random.choice(s); s.remove(das1)
        das2 = random.choice(s); s.remove(das2)
        das3 = random.choice(s)
        noidungcauhoi = 'Cho mệnh đề chứa biến $P(n)=n^2-1$. Mệnh đề nào sau đây là đúng?. \n'
        da_d = '\\True ' + str(da)
        da_s1, da_s2, da_s3 = str(das1), str(das2), str(das3)
        loigiai = '$P(2)=2^2-1=3$ nên chia hết cho 3.'

    elif dang == '3':
        du = ['$P(3)$ chia hết cho 8']
        da = random.choice(du)
        s = ['$P(1)$ không chia hết cho 3', '$P(6)$ chia hết cho 5', '$P(8)$ không chia hết cho 3', '$P(11)$ không chia hết cho 2', '$P(12)$ chia hết cho 10', '$P(5)$ không chia hết cho 8', '$P(2)$ không chia hết cho 3', ' $P(9)$ không chia hết cho 4', '$P(4)$ chia hết cho 4', '$P(10)$ chia hết cho 10', '$P(7)$ chia hết cho 5']
        das1 = random.choice(s); s.remove(das1)
        das2 = random.choice(s); s.remove(das2)
        das3 = random.choice(s)
        noidungcauhoi = 'Cho mệnh đề chứa biến $P(n)=n^2-1$. Mệnh đề nào sau đây là đúng?. \n'
        da_d = '\\True ' + str(da)
        da_s1, da_s2, da_s3 = str(das1), str(das2), str(das3)
        loigiai = '$P(3)=3^2-1=8$ nên chia hết cho 8.'

    elif dang == '4':
        du = ['$P(4)$ không chia hết cho 4']
        da = random.choice(du)
        s = ['$P(1)$ không chia hết cho 3', '$P(6)$ chia hết cho 5', '$P(8)$ không chia hết cho 3', '$P(11)$ không chia hết cho 2', '$P(12)$ chia hết cho 10', '$P(5)$ không chia hết cho 8', '$P(2)$ không chia hết cho 3', ' $P(9)$ không chia hết cho 4', '$P(4)$ chia hết cho 4', '$P(10)$ chia hết cho 10', '$P(3)$ không chia hết cho 8', '$P(7)$ chia hết cho 5']
        das1 = random.choice(s); s.remove(das1)
        das2 = random.choice(s); s.remove(das2)
        das3 = random.choice(s)
        noidungcauhoi = 'Cho mệnh đề chứa biến $P(n)=n^2-1$. Mệnh đề nào sau đây là đúng?. \n'
        da_d = '\\True ' + str(da)
        da_s1, da_s2, da_s3 = str(das1), str(das2), str(das3)
        loigiai = '$P(4)=4^2-1=15$ nên không chia hết cho 4.'

    elif dang == '5':
        du = ['$P(5)$ chia hết cho 8']
        da = random.choice(du)
        s = ['$P(1)$ không chia hết cho 3', '$P(6)$ chia hết cho 5', '$P(8)$ không chia hết cho 3', '$P(11)$ không chia hết cho 2', '$P(12)$ chia hết cho 10', '$P(2)$ không chia hết cho 3', ' $P(9)$ không chia hết cho 4', '$P(4)$ chia hết cho 4', '$P(10)$ chia hết cho 10', '$P(3)$ không chia hết cho 8', '$P(7)$ chia hết cho 5']
        das1 = random.choice(s); s.remove(das1)
        das2 = random.choice(s); s.remove(das2)
        das3 = random.choice(s)
        noidungcauhoi = 'Cho mệnh đề chứa biến $P(n)=n^2-1$. Mệnh đề nào sau đây là đúng?. \n'
        da_d = '\\True ' + str(da)
        da_s1, da_s2, da_s3 = str(das1), str(das2), str(das3)
        loigiai = '$P(5)=5^2-1=24$ nên chia hết cho 8.'

    elif dang == '6':
        du = ['$P(6)$ không chia hết cho 6']
        da = random.choice(du)
        s = ['$P(1)$ không chia hết cho 3', '$P(8)$ không chia hết cho 3', '$P(11)$ không chia hết cho 2', '$P(12)$ chia hết cho 10', '$P(5)$ không chia hết cho 8', '$P(2)$ không chia hết cho 3', ' $P(9)$ không chia hết cho 4', '$P(4)$ chia hết cho 4', '$P(10)$ chia hết cho 10', '$P(3)$ không chia hết cho 8', '$P(7)$ chia hết cho 5']
        das1 = random.choice(s); s.remove(das1)
        das2 = random.choice(s); s.remove(das2)
        das3 = random.choice(s)
        noidungcauhoi = 'Cho mệnh đề chứa biến $P(n)=n^2-1$. Mệnh đề nào sau đây là đúng?. \n'
        da_d = '\\True ' + str(da)
        da_s1, da_s2, da_s3 = str(das1), str(das2), str(das3)
        loigiai = '$P(6)=6^2-1=35$ nên không chia hết cho 6.'

    elif dang == '7':
        du = ['$P(7)$ không chia hết cho 5']
        da = random.choice(du)
        s = ['$P(1)$ không chia hết cho 3', '$P(6)$ chia hết cho 5', '$P(8)$ không chia hết cho 3', '$P(11)$ không chia hết cho 2', '$P(12)$ chia hết cho 10', '$P(5)$ không chia hết cho 8', '$P(2)$ không chia hết cho 3', ' $P(9)$ không chia hết cho 4', '$P(4)$ chia hết cho 4', '$P(10)$ chia hết cho 10', '$P(3)$ không chia hết cho 8']
        das1 = random.choice(s); s.remove(das1)
        das2 = random.choice(s); s.remove(das2)
        das3 = random.choice(s)
        noidungcauhoi = 'Cho mệnh đề chứa biến $P(n)=n^2-1$. Mệnh đề nào sau đây là đúng?. \n'
        da_d = '\\True ' + str(da)
        da_s1, da_s2, da_s3 = str(das1), str(das2), str(das3)
        loigiai = '$P(7)=7^2-1=48$ nên không chia hết cho 5.'

    elif dang == '8':
        du = ['$P(8)$ chia hết cho 3']
        da = random.choice(du)
        s = ['$P(1)$ không chia hết cho 3', '$P(6)$ chia hết cho 5', '$P(11)$ không chia hết cho 2', '$P(12)$ chia hết cho 10', '$P(5)$ không chia hết cho 8', '$P(2)$ không chia hết cho 3', ' $P(9)$ không chia hết cho 4', '$P(4)$ chia hết cho 4', '$P(10)$ chia hết cho 10', '$P(3)$ không chia hết cho 8', '$P(7)$ chia hết cho 5']
        das1 = random.choice(s); s.remove(das1)
        das2 = random.choice(s); s.remove(das2)
        das3 = random.choice(s)
        noidungcauhoi = 'Cho mệnh đề chứa biến $P(n)=n^2-1$. Mệnh đề nào sau đây là đúng?. \n'
        da_d = '\\True ' + str(da)
        da_s1, da_s2, da_s3 = str(das1), str(das2), str(das3)
        loigiai = '$P(8)=8^2-1=63$ nên chia hết cho 3.'

    elif dang == '9':
        du = ['$P(9)$ chia hết cho 4']
        da = random.choice(du)
        s = ['$P(1)$ không chia hết cho 3', '$P(6)$ chia hết cho 5', '$P(8)$ không chia hết cho 3', '$P(11)$ không chia hết cho 2', '$P(12)$ chia hết cho 10', '$P(5)$ không chia hết cho 8', '$P(2)$ không chia hết cho 3', '$P(4)$ chia hết cho 4', '$P(10)$ chia hết cho 10', '$P(3)$ không chia hết cho 8', '$P(7)$ chia hết cho 5']
        das1 = random.choice(s); s.remove(das1)
        das2 = random.choice(s); s.remove(das2)
        das3 = random.choice(s)
        noidungcauhoi = 'Cho mệnh đề chứa biến $P(n)=n^2-1$. Mệnh đề nào sau đây là đúng?. \n'
        da_d = '\\True ' + str(da)
        da_s1, da_s2, da_s3 = str(das1), str(das2), str(das3)
        loigiai = '$P(9)=9^2-1=80$ nên chia hết cho 4.'

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ 
        '\\choice \n'
        '{'+str(list_1[1])+'}\n'
        '{'+str(list_1[2])+'}\n'
        '{'+str(list_1[3])+'}\n'
        '{'+str(list_1[0])+'}\n'
        '\\loigiai{'+str(loigiai)+'}\n'
        '\\end{ex}\n\\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('++','+').replace('--','+').replace('+-','-').replace('-+','-').replace('10x','10 x').replace('+0x','').replace('-0x','').replace('11x','11 x').replace('1x','x').replace('10y','10 y').replace('+0y','').replace('-0y','').replace('11y','11 y').replace('1y','y').replace('10t','10 t').replace('+0t','').replace('-0t','').replace('11t','11 t').replace('1t','t')
    return content

