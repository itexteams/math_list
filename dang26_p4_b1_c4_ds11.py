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


def bt_dang26_p4_b1_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B1 & B3: Thiết lập thông số ngẫu nhiên
                b_val = random.randrange(4, 12, 2) # Chọn số chẵn dương để biểu thức là n^2 - bn
                c_val = random.randint(5, 20)
                a_correct = b_val // 2 # Giá trị để lim = 0

                # Đáp án trắc nghiệm
                da = '$%s$' % latex(a_correct)
                s = list(set([a_correct + 1, a_correct - 1, a_correct + 2, 0]))
                if a_correct in s: s.remove(a_correct)
                random.shuffle(s)
                das1, das2, das3 = '$%s$'%s[0], '$%s$'%s[1], '$%s$'%s[2]

                # Nội dung câu hỏi
                noidungcauhoi = (r'''Tìm giá trị của $a$ để $\lim\limits_{{n\to +\infty}} \left(\sqrt{n^2 - %s n + %s} + a - n\right) = 0$.''' 
                                 % (latex(b_val), latex(c_val)))

                # B2- Lời giải: Sửa lỗi tử số sau dấu bằng thứ 3 (phải chia cho n)
                # Đếm chính xác 17 vị trí %s
                loigiai = (r'''$\lim\limits_{{n\to +\infty}} \left(\sqrt{n^2 - %s n + %s} + a - n\right) = \lim\limits_{{n\to +\infty}} \frac{n^2 - %s n + %s - (n - a)^2}{\sqrt{n^2 - %s n + %s} - (a - n)}$ \\
            $= \lim\limits_{{n\to +\infty}} \frac{- %s n + %s + 2an - a^2}{\sqrt{n^2 - %s n + %s} - (a - n)} = \lim\limits_{{n\to +\infty}} \frac{(2a - %s) + \frac{%s - a^2}{n}}{\sqrt{1 - \frac{%s}{n} + \frac{%s}{n^2}} - \frac{a}{n} + 1}$ \\
            $= \frac{2a - %s}{2} = a - %s$. \\
            Để $\lim\limits_{{n\to +\infty}} \left(\sqrt{n^2 - %s n + %s} + a - n\right) = 0$ thì $a - %s = 0 \Leftrightarrow a = %s$.''' 
                           % (latex(b_val), latex(c_val), # Dòng 1
                              latex(b_val), latex(c_val), # Dòng 1 tử
                              latex(b_val), latex(c_val), # Dòng 1 mẫu
                              latex(b_val), latex(c_val), # Dòng 2 tử
                              latex(b_val), latex(c_val), # Dòng 2 mẫu
                              latex(b_val), latex(c_val), # Dòng 2 sau dấu = thứ 3 (Tử đã chia n)
                              latex(b_val), latex(c_val), # Dòng 2 mẫu chia n
                              latex(b_val), latex(a_correct), # Dòng 3
                              latex(b_val), latex(c_val), # Dòng 4
                              latex(a_correct), latex(a_correct))) # Dòng 4 cuối

                # Các đáp án
                da_d = ('\\True ' + str(da))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

