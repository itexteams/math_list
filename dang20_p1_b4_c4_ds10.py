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


def bt_dang20_p1_b4_c4_ds10(self):
            # Khai báo biến
            # Trong ảnh k = 15 => R^2 = 16 => R = 4.
            R = randint(3, 6) 
            k = R**2 - 1

            # Điều kiện để có nghiệm duy nhất: m = 1 - R
            m_val = 1 - R

            # Tạo các phương án trắc nghiệm
            # Đáp án đúng là một khoảng chứa m_val
            correct_interval = '$m \\in (%s;%s)$' % (latex(m_val - 1), latex(m_val + 1))
            da_d = '\\True ' + correct_interval

            # Các đáp án sai
            s1 = '$m \\in (%s;%s)$' % (latex(m_val + 1), latex(m_val + 3))
            s2 = '$m = %s$' % (latex(m_val - 1))
            s3 = '$m = -\\frac{%s}{4}$' % (latex(4*abs(m_val) + 13)) # Tạo một phân số trông phức tạp

            list_1 = [da_d, s1, s2, s3]
            random.shuffle(list_1)

            # Bước 2: Viết lại đề bài và lời giải chi tiết
            noidungcauhoi = ('''Nếu phương trình $x^2 + 2x + \\sqrt{-x^2 - 2x + %s} + m = 0$ có nghiệm duy nhất thì'''
                            %(latex(k)))

            # Tính toán các giá trị cho lời giải
            # x^2 + 2x + 15 = -(x+5)(3-x) + 15 -> Tổng quát: x^2 + 2x + k = -(x + (R+1))( (R-1) - x) + k
            # Ở đây dùng dạng hằng đẳng thức để dễ theo dõi: -(x+1)^2 + R^2
            root_expr = '(%s+x)(%s-x)' % (latex(R+1), latex(R-1))

            loigiai = ('''Phương trình tương đương với:
                        $-(x+%s)(%s-x) + \\sqrt{(x+%s)(%s-x)} + m + %s = 0 \\quad (1)$ \\\\
                        Nhận xét: Nếu $a$ là nghiệm của (1) thì $-2-a$ cũng là nghiệm của (1). \\\\
                        Để (1) có nghiệm duy nhất thì $a = -2 - a \\Leftrightarrow a = -1$. \\\\
                        Thay $a = -1$ là nghiệm của (1), ta có: \\\\
                        $(-1)^2 + 2(-1) + \\sqrt{-(-1)^2 - 2(-1) + %s} + m = 0 \\\\
                        \\Leftrightarrow 1 - 2 + \\sqrt{1 + 2 + %s} + m = 0 \\\\
                        \\Leftrightarrow -1 + \\sqrt{%s} + m = 0 \\\\
                        \\Leftrightarrow -1 + %s + m = 0 \\Leftrightarrow m = %s$. \\\\
                        Thử lại: Thay $m = %s$ vào phương trình ban đầu, ta được nghiệm duy nhất $x = -1$. \\\\
                        Vì $m = %s$ nên ta chọn phương án chứa giá trị này.'''
                        %(latex(R+1), latex(R-1), latex(R+1), latex(R-1), latex(k),
                          latex(k), latex(k), latex(R**2), latex(R), latex(m_val), 
                          latex(m_val), latex(m_val)))

            # Bước 4: Xuất nội dung theo cấu trúc mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

