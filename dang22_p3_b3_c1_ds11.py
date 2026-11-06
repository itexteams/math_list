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


def bt_dang22_p3_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random hệ số gắn với m (ví dụ: 2, 3, 4, 5) và góc (ví dụ: 3x, 4x, 5x) của hàm sin
                # Random góc của hàm cos (ví dụ: 2x, 3x)
                heso_m = random.choice([2, 3, 4, 5])
                goc_sin = random.choice([3, 4, 5])
                goc_cos = random.choice([2, 3])

                # Chuỗi hiển thị cho các thành phần trong bài toán
                ham_goc = '%sm\\sin %sx + \\cos %sx' % (latex(heso_m), latex(goc_sin), latex(goc_cos))
                f_am_x = 'f(-x) = %sm\\sin %s(-x) + \\cos %s(-x) = -%sm\\sin %sx + \\cos %sx' % (latex(heso_m), latex(goc_sin), latex(goc_cos), latex(heso_m), latex(goc_sin), latex(goc_cos))

                buoc_tuong_duong1 = '-%sm\\sin %sx + \\cos %sx = %sm\\sin %sx + \\cos %sx, \\forall x \\in D' % (latex(heso_m), latex(goc_sin), latex(goc_cos), latex(heso_m), latex(goc_sin), latex(goc_cos))
                buoc_tuong_duong2 = '%sm\\sin %sx = 0, \\forall x \\in D \\Leftrightarrow m = 0' % (latex(2 * heso_m), latex(goc_sin))

                # Câu hỏi sử dụng %s đúng cấu trúc mẫu
                noidungcauhoi = ('''Giá trị của tham số $m$ để hàm số $y = f(x) = %s$ là hàm số chẵn bằng bao nhiêu?''' % (str(ham_goc)))

                # Đáp án đúng
                da = '$m = 0$'
                da_d = ('\\True ' + str(da))

                # Các đáp án sai ngẫu nhiên và không trùng đáp án đúng
                s = ['$m > 0$', '$m < -1$', '$m = 2$', '$m < 0$', '$m = 1$', '$m = -2$']
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Đưa các đáp án vào danh sách và trộn ngẫu nhiên
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết theo các bước như ảnh gốc, sử dụng %s
                loigiai = ('''Tập xác định: $D = \\mathbb{R}$. Suy ra $\\forall x \\in D \\Rightarrow -x \\in D$. \\\\
                           Ta có $%s$. \\\\
                           Để hàm số đã cho là hàm số chẵn thì \\\\
                           $f(-x) = f(x), \\forall x \\in D \\Leftrightarrow %s \\\\
                           \\Leftrightarrow %s$.'''
                           % (str(f_am_x), str(buoc_tuong_duong1), str(buoc_tuong_duong2)))
                dapan='\\shortans[0]{$%s$}\n'%(latex(0))

            # Xuất câu trắc nghiệm hoàn chỉnh theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

