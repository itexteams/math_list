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


def bt_dang2_p4_b3_c2_ds11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                n=randint(5,12)
                a=Rational(2**n-1,2**n)
                x0=Rational(2*a,1-a)
                h1=1

                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Đầu mùa thu hoạch dưa hấu, ông Nam đã bán cho người thứ nhất một nửa số dưa hấu thu hoạch được và tặng thêm $1$ quả, bán cho người thứ hai nữa số dứa hấu còn lại và tặng thêm $1$ quả. Ông tứ tiếp tục cách bán như trên thì đến người thứ $%s$ số dưa hấu của ông được bán hết. Tính số dưa hấu mà ông Nam thu hoạch được. \n'
                                %(latex(n)
                                ))

                # Nội dung lời giải
                loigiai = ('Gọi $x$ là số dưa hấu mà ông Nam thu hoạch được, $(x>0)$. \\\\ \n'
                        'Khi đó \\\\ \n'
                        '\\hspace*{1cm} Số quả dưa hấu mà người thứ nhất mua và được tặng là $\\dfrac{1}{2}x+1=\\dfrac{x+2}{2}$.\\\\ \n'
                        '\\hspace*{1cm} Số quả dưa hấu mà người thứ hai mua và được tặng là $\\dfrac{1}{2} \\left( x-\\frac{x+2}{2} \\right)+1=\\dfrac{x+2}{2^2}$.\\\\ \n'
                        '\\hspace*{1cm} Tiếp tục như vậy \\\\ \n'
                        '\\hspace*{1cm} Số quả dưa hấu mà người thứ $%s$ mua và được tặng là $\\dfrac{x+2}{2^{%s}}$.\\\\ \n'
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $\\frac{x+2}{2}+\\frac{x+2}{2^2}+\\cdots+\\frac{x+2}{2^{%s}}=x$. \\\\ \n'
                        '\\hspace*{1cm} $\\Leftrightarrow (x+2) \\left( \\frac{1}{2}+\\frac{1}{2^2}+\\cdots+\\frac{1}{2^{%s}} \\right)=x$. \\\\ \n'
                        '\\hspace*{1cm} $\\Leftrightarrow (x+2) \\frac{1}{2} \\cdot \\left( \\frac{1-\\left( \\frac{1}{2} \\right)^{%s} }{1-\\frac{1}{2}} \\right)=x$.\\\\ \n'
                        '\\hspace*{1cm} $\\Leftrightarrow %s (x+2)=x$.\\\\ \n'
                        '\\hspace*{1cm} $\\Leftrightarrow x=%s$.\\\\ \n'
                        'Vậy số dưa hấu ông Nam thu hoạch được là $%s$ quả.'
                        %(latex(n),latex(n),
                            latex(n),latex(n),
                            latex(n),
                            latex(a),latex(x0),
                            latex(x0)
                            ))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content                

