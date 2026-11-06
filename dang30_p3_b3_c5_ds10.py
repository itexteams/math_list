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


def bt_dang30_p3_b3_c5_ds10(self):
            # Để kết quả 2^(n-1) < 9999, n tối đa là 14
            n = random.randint(6, 14)

            # Tính giá trị số nguyên của tổng T = 2^(n-1)
            kq_val = 2**(n - 1)

            # Xác định số hạng cuối cùng hiển thị trong chuỗi tổng (phụ thuộc n chẵn/lẻ)
            if n % 2 == 0:
                last_term = "C_{%s}^{%s}" % (n, n)
            else:
                last_term = "C_{%s}^{%s}" % (n, n - 1)

            # Câu hỏi
            noidungcauhoi = ('''Tổng $T = C_{%s}^0 + C_{%s}^2 + C_{%s}^4 + \\dots + %s$ bằng bao nhiêu?'''
                             % (n, n, n, last_term))

            # Đáp án đúng
            da_dung = '\\True $%s$' % (latex(kq_val))

            # Tạo các phương án nhiễu (số nguyên)
            s_set = set()
            while len(s_set) < 3:
                # Các sai lầm phổ biến: tính 2^n, 2^(n-2), hoặc sai lệch đơn vị
                sai_2n = 2**n
                sai_n2 = 2**(n - 2)
                offset = random.choice([1, -1, 10, 100])

                nhieu = random.choice([sai_2n, sai_n2, kq_val + offset])
                if nhieu != kq_val and 0 < nhieu < 20000:
                    s_set.add('$%s$' % (latex(nhieu)))

            list_ans = [da_dung] + list(s_set)
            random.shuffle(list_ans)

            # Nội dung lời giải chi tiết
            loigiai = ('''Xét khai triển nhị thức Newton: \\\\
                         $(1+x)^{%s} = C_{%s}^0 + C_{%s}^1 x + C_{%s}^2 x^2 + \\dots + C_{%s}^{%s} x^{%s}$. \\\\
                         - Thay $x=1$, ta được: $2^{%s} = C_{%s}^0 + C_{%s}^1 + C_{%s}^2 + \\dots + C_{%s}^{%s}$ (1). \\\\
                         - Thay $x=-1$, ta được: $0 = C_{%s}^0 - C_{%s}^1 + C_{%s}^2 - \\dots + (-1)^{%s} C_{%s}^{%s}$ (2). \\\\
                         Cộng vế với vế của (1) và (2) ta được: \\\\
                         $2^{%s} = 2(C_{%s}^0 + C_{%s}^2 + C_{%s}^4 + \\dots) = 2T$. \\\\
                         Vậy $T = \\frac{2^{%s}}{2} = 2^{%s} = %s$.'''
                       % (n, n, n, n, n, n, n, 
                          n, n, n, n, n, n, 
                          n, n, n, n, n, n, 
                          n, n, n, n, 
                          n, n-1, latex(kq_val)))

            # Đáp án ngắn (Điền số nguyên kq_val)
            dapan = '\\shortans[0]{$%s$}\n' % (latex(kq_val))

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + noidungcauhoi + dapan +
                       '\\loigiai{' + loigiai + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')

            return content

