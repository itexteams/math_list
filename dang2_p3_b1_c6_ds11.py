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


def bt_dang2_p3_b1_c6_ds11(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)

            if dang=='2':
                n=16
                def is_prime(m):
                    if m < 2:
                        return False
                    for i in range(2, int(m ** 0.5) + 1):
                        if m % i == 0:
                            return False
                    return True
                m=Rational(n,2)
                so_nguyen_to = [i for i in range(1, n) if is_prime(i)]
                KGM = [i for i in range(1, n)]
                so_le = [i for i in range(1, n) if i % 2 != 0]

                so_chan = [i for i in range(1, n) if i % 2 == 0 and i>m]
                so_B = [i for i in range(1, n) if i >=m and i<=n-1]

                hop_AB = set(so_le) | set(so_nguyen_to)
                giao_AB = set(so_chan) & set(so_B)
                kq=len(giao_AB)

                # Câu hỏi
                noidungcauhoi = ('''Một hộp đựng $%s$ tấm thẻ cùng loại được đánh số từ $1$ đến $%s$. Rút ngẫu nhiên một tấm thẻ trong hộp. Gọi $A$ là biến cố "Rút được tấm thẻ ghi số chẵn lớn hơn $%s$"; $B$ là biến cố "Rút được tấm thẻ ghi số không nhỏ hơn $%s$ và không lớn hơn $%s$". Số phần tử của biến cố $A\\cap B$ bằng bao nhiêu?'''
                                %(latex(n-1),latex(n-1),latex(m),latex(m),latex(n-1)
                                ))

                # Nội dung lời giải
                loigiai=('''Ta có \\\\
                        Không gian mẫu $\\Omega ={%s}$. \\\\
                        Biến cố $A={%s}$. \\\\
                            Biến cố $B={%s}$. \\\\
                                Vậy biến cố $A \\cap B ={%s}$ và có số phần tử là $%s$.'''
                        %(latex(KGM),latex(so_chan),latex(so_B),latex(giao_AB),latex(kq)
                        ))   
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))            

            if dang=='1':
                n=randint(6,16)
                def is_prime(m):
                    if m < 2:
                        return False
                    for i in range(2, int(m ** 0.5) + 1):
                        if m % i == 0:
                            return False
                    return True

                so_nguyen_to = [i for i in range(1, n) if is_prime(i)]
                KGM = [i for i in range(1, n)]
                so_le = [i for i in range(1, n) if i % 2 != 0]

                hop_AB = set(so_le) | set(so_nguyen_to)
                giao_AB = set(so_le) & set(so_nguyen_to)
                kq=len(giao_AB)

                # Câu hỏi
                noidungcauhoi = ('''Một hộp đựng $%s$ tấm thẻ cùng loại được đánh số từ $1$ đến $%s$. Rút ngẫu nhiên một tấm thẻ trong hộp. Gọi $A$ là biến cố "Số ghi trên tấm thẻ là số lẻ"; $B$ là biến cố "Số ghi trên tấm thẻ là số nguyên tố". Số phần tử của biến cố $A\\cap B$ bằng bao nhiêu?'''
                                %(latex(n-1),latex(n-1)
                                ))

                # Nội dung lời giải
                loigiai=('''Ta có \\\\
                        Không gian mẫu $\\Omega ={%s}$. \\\\
                        Biến cố $A={%s}$. \\\\
                            Biến cố $B={%s}$. \\\\
                                Vậy biến cố $A \\cap B ={%s}$ và có số phần tử là $%s$.'''
                        %(latex(KGM),latex(so_le),latex(so_nguyen_to),latex(giao_AB),latex(kq)
                        ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+    
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\left[', '\\left\\lbrace').replace('\\right]', '\\right\\rbrace').replace(',', ';')
            return content

