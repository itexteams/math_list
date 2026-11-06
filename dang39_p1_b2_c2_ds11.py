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


def bt_dang39_p1_b2_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random m để n = m^2 - 2 luôn cho ra k là số nguyên
                m_list = [3, 4, 5, 6]
                m = random.choice(m_list)
                n = m**2 - 2

                # Tính các nghiệm k
                k1 = (n - 2 - m) // 2
                k2 = (n - 2 + m) // 2

                # Tổng phần tử
                sum_k = k1 + k2

                # Các đáp án trắc nghiệm
                da = '$%s$' % sum_k

                # Các phương án sai
                s = [
                    '$%s$' % (sum_k - 2),
                    '$%s$' % (sum_k + 2),
                    '$%s$' % (sum_k - 4),
                    '$%s$' % (sum_k + 4),
                    '$%s$' % (k1 * k2)
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Gọi $S$ là tập hợp tất cả các số tự nhiên $k$ sao cho $C_{%s}^k, C_{%s}^{k+1}, C_{%s}^{k+2}$ theo thứ tự đó lập thành một cấp số cộng. Tổng tất cả các phần tử của $S$ là''' % (n, n, n))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai=('''Điều kiện: $0 \\le k \\le %s$, $k \\in \\mathbb{N}$. \\\\
                         Để ba số $C_{%s}^k, C_{%s}^{k+1}, C_{%s}^{k+2}$ lập thành một cấp số cộng thì: \\\\
                         $C_{%s}^k + C_{%s}^{k+2} = 2C_{%s}^{k+1}$ \\\\
                         $\\Leftrightarrow \\frac{%s!}{k!(%s-k)!} + \\frac{%s!}{(k+2)!(%s-k-2)!} = 2\\frac{%s!}{(k+1)!(%s-k-1)!}$ \\\\
                         Chia cả hai vế cho $\\frac{%s!}{(k+1)!(%s-k-1)!}$ ta được: \\\\
                         $\\frac{k+1}{%s-k} + \\frac{%s-k-1}{k+2} = 2$ \\\\
                         $\\Leftrightarrow (k+1)(k+2) + (%s-k)(%s-k-1) = 2(%s-k)(k+2)$ \\\\
                         $\\Leftrightarrow k^2 + 3k + 2 + k^2 - (2 \\cdot %s - 1)k + %s^2 - %s = -2k^2 + 2(%s - 2)k + 4 \\cdot %s$ \\\\
                         $\\Leftrightarrow 4k^2 - 4k(%s) + %s = 0$ \\\\
                         $\\Leftrightarrow \\left[ \\begin{array}{l} k = %s \\\\ k = %s \\end{array} \\right.$ (thỏa mãn điều kiện). \\\\
                         Vậy $S = \\{%s; %s\\}$. Tổng tất cả các phần tử của $S$ là $%s + %s = %s$.'''
                         % (n-2, 
                            n, n, n,
                            n, n, n,
                            n, n, n, n, n, n,
                            n, n,
                            n, n,
                            n, n, n,
                            n, n, n, n, n,
                            n-2, n**2 - 5*n + 2,
                            k1, k2,
                            k1, k2, k1, k2, sum_k))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

