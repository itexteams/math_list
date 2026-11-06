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


def bt_dang16_p4_b1_c6_ds10(self):
            # Khai báo biến
            lis=['Số chấm xuất hiện bằng nhau','Tổng số chấm xuất hiện bằng $8$','Mặt xuất hiện cùng chia hết cho $3$','Hai mặt xuất hiện có tổng chia hết cho $3$','Mặt xuất hiện lần thứ hai gấp đôi lần thứ nhất','Tổng số chấm xuất hiện chia hết cho $5$']
            bc=random.choice(lis)
            # Câu hỏi
            noidungcauhoi='''Gieo một con xúc sắc cân đối và đồng chất hai lần. Gọi $A$ là biến cố "%s". Tính xác suất của biến cố $A$.'''%(str(bc))
            # Các đáp án
            if bc=='Số chấm xuất hiện bằng nhau':
                da_d = '\\True $\\mathrm{P}(A)=\\dfrac{1}{6}$'
                da_s1 = '$\\mathrm{P}(A)=\\dfrac{5}{6}$'
                da_s2 = '$\\mathrm{P}(A)=\\dfrac{1}{3}$'
                da_s3 = '$\\mathrm{P}(A)=\\dfrac{2}{3}$'
            if bc=='Tổng số chấm xuất hiện bằng $8$':
                da_d = '\\True $\\mathrm{P}(A)=\\dfrac{5}{36}$'
                da_s1 = '$\\mathrm{P}(A)=\\dfrac{7}{36}$'
                da_s2 = '$\\mathrm{P}(A)=\\dfrac{31}{36}$'
                da_s3 = '$\\mathrm{P}(A)=\\dfrac{11}{36}$'
            if bc=='Mặt xuất hiện cùng chia hết cho $3$':
                da_d = '\\True $\\mathrm{P}(A)=\\dfrac{1}{9}$'
                da_s1 = '$\\mathrm{P}(A)=\\dfrac{2}{9}$'
                da_s2 = '$\\mathrm{P}(A)=\\dfrac{5}{9}$'
                da_s3 = '$\\mathrm{P}(A)=\\dfrac{7}{9}$'
            if bc=='Hai mặt xuất hiện có tổng chia hết cho $3$':
                da_d = '\\True $\\mathrm{P}(A)=\\dfrac{1}{3}$'
                da_s1 = '$\\mathrm{P}(A)=\\dfrac{2}{3}$'
                da_s2 = '$\\mathrm{P}(A)=\\dfrac{1}{4}$'
                da_s3 = '$\\mathrm{P}(A)=\\dfrac{3}{4}$'
            if bc=='Mặt xuất hiện lần thứ hai gấp đôi lần thứ nhất':
                da_d = '\\True $\\mathrm{P}(A)=\\dfrac{1}{12}$'
                da_s1 = '$\\mathrm{P}(A)=\\dfrac{5}{12}$'
                da_s2 = '$\\mathrm{P}(A)=\\dfrac{1}{6}$'
                da_s3 = '$\\mathrm{P}(A)=\\dfrac{5}{6}$'
            if bc=='Tổng số chấm xuất hiện chia hết cho $5$':
                da_d = '\\True $\\mathrm{P}(A)=\\dfrac{7}{36}$'
                da_s1 = '$\\mathrm{P}(A)=\\dfrac{5}{36}$'
                da_s2 = '$\\mathrm{P}(A)=\\dfrac{7}{12}$'
                da_s3 = '$\\mathrm{P}(A)=\\dfrac{5}{12}$'
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d,da_s1,da_s2,da_s3]
            random.shuffle(list_1)
            # Nội dung lời giải
            if bc=='Số chấm xuất hiện bằng nhau':
                loigiai=('Số phần tử của không gian mẫu là $n(\\Omega)=36.$ \\\\ \n'
                    'Ta có $A=\\left\\{ (1,1);(2,2);(3,3);(4,4);(5,5);(6,6) \\right\\}$.\\\\ \n' 
                    'Suy ra $n(A)=6$. Xác suất của biến cố $A$ là $\\mathrm{P}(A)=\\dfrac{6}{36}=\\dfrac{1}{6}$.')
            if bc=='Tổng số chấm xuất hiện bằng $8$':
                loigiai=('Số phần tử của không gian mẫu là $n(\\Omega)=36.$ \\\\ \n'
                    'Ta có $A=\\left\\{ (2,6);(3,5);(4,4);(5,3);(6,2) \\right\\}$.\\\\ \n'
                    'Suy ra $n(A)=5$. Xác suất của biến cố $A$ là $\\mathrm{P}(A)=\\dfrac{5}{36}$.')
            if bc=='Mặt xuất hiện cùng chia hết cho $3$':
                loigiai=('Số phần tử của không gian mẫu là $n(\\Omega)=36.$ \\\\ \n'
                    'Ta có $A=\\left\\{ (3,3);(3,6);(6,3);(6,6) \\right\\}$.\\\\ \n' 
                    'Suy ra $n(A)=4$. Xác suất của biến cố $A$ là $\\mathrm{P}(A)=\\dfrac{4}{36}=\\dfrac{1}{9}$.')
            if bc=='Hai mặt xuất hiện có tổng chia hết cho $3$':
                loigiai=('Số phần tử của không gian mẫu là $n(\\Omega)=36.$ \\\\ \n'
                    'Ta có $A=\\left\\{ (1,2);(1,5);(2,1);(2,4);(3,3);(3,6);(4,2);(4,5);(5,1);(5,4);(6,3);(6,6) \\right\\}$.\\\\ \n' 
                    'Suy ra $n(A)=12$. Xác suất của biến cố $A$ là $\\mathrm{P}(A)=\\dfrac{12}{36}=\\dfrac{1}{3}$.')
            if bc=='Mặt xuất hiện lần thứ hai gấp đôi lần thứ nhất':
                loigiai=('Số phần tử của không gian mẫu là $n(\\Omega)=36.$ \\\\ \n'
                    'Ta có $A=\\left\\{ (1,2);(2,4);(3,6) \\right\\}$.\\\\ \n' 
                    'Suy ra $n(A)=3$. Xác suất của biến cố $A$ là $\\mathrm{P}(A)=\\dfrac{3}{36}=\\dfrac{1}{12}$.')
            if bc=='Tổng số chấm xuất hiện chia hết cho $5$':
                loigiai=('Số phần tử của không gian mẫu là $n(\\Omega)=36.$ \\\\ \n'
                    'Ta có $A=\\left\\{ (1,4);(2,3);(3,2);(4,1);(4,6);(5,5);(6,4) \\right\\}$.\\\\ \n' 
                    'Suy ra $n(A)=7$. Xác suất của biến cố $A$ là $\\mathrm{P}(A)=\\dfrac{7}{36}$.')
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

