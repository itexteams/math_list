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


def bt_dang10_p3_b1_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Random tham số tỉ lệ k1 = MA/MD và k2 = GD/GN
        k1 = random.choice([1, 2, 3])
        k2 = random.choice([2, 3, 4])

        # Tính toán kết quả
        k_prod = k1 * k2
        kq_val = k_prod - 1

        # Đáp án đúng
        kq = latex(kq_val)

        # Tạo các phương án sai không trùng đáp án đúng
        s_wrong = []
        candidates = [k_prod, k_prod + 1, kq_val + 1, kq_val + 2, kq_val + 3, abs(kq_val - 2)]
        for c in candidates:
            if c != kq_val and c not in s_wrong and c > 0:
                s_wrong.append(c)

        das_list = random.sample(s_wrong, 3)

        da = '$%s$' % (kq)
        das1 = '$%s$' % (latex(das_list[0]))
        das2 = '$%s$' % (latex(das_list[1]))
        das3 = '$%s$' % (latex(das_list[2]))

        # Tạo nội dung câu hỏi sử dụng định dạng %s
        if k1 == 1 and k2 == 2:
            noidungcauhoi = ('''Cho tứ diện $ABCD$. Gọi $M, N$ lần lượt là trung điểm của các cạnh $%s, %s$, điểm $G$ là trọng tâm của tam giác $%s$. Gọi $I$ là giao điểm của đường thẳng $MG$ và mặt phẳng $(ABC)$. Khi đó tỉ lệ $\\frac{AN}{NI}$ bằng bao nhiêu?'''
                             % ('AD', 'BC', 'BCD'))
        elif k1 > 1 and k2 == 2:
            noidungcauhoi = ('''Cho tứ diện $ABCD$. Gọi $N$ là trung điểm của cạnh $BC$, $M$ là điểm thuộc cạnh $AD$ sao cho $MA = %s MD$, điểm $G$ là trọng tâm của tam giác $BCD$. Gọi $I$ là giao điểm của đường thẳng $MG$ và mặt phẳng $(ABC)$. Khi đó tỉ lệ $\\frac{AN}{NI}$ bằng bao nhiêu?'''
                             % (latex(k1)))
        elif k1 == 1 and k2 > 2:
            noidungcauhoi = ('''Cho tứ diện $ABCD$. Gọi $M, N$ lần lượt là trung điểm của các cạnh $%s, %s$, điểm $G$ thuộc đoạn thẳng $DN$ sao cho $GD = %s GN$. Gọi $I$ là giao điểm của đường thẳng $MG$ và mặt phẳng $(ABC)$. Khi đó tỉ lệ $\\frac{AN}{NI}$ bằng bao nhiêu?'''
                             % ('AD', 'BC', latex(k2)))
        else:
            noidungcauhoi = ('''Cho tứ diện $ABCD$. Gọi $N$ là trung điểm của cạnh $BC$, $M$ là điểm thuộc cạnh $AD$ sao cho $MA = %s MD$, điểm $G$ thuộc đoạn thẳng $DN$ sao cho $GD = %s GN$. Gọi $I$ là giao điểm của đường thẳng $MG$ và mặt phẳng $(ABC)$. Khi đó tỉ lệ $\\frac{AN}{NI}$ bằng bao nhiêu?'''
                             % (latex(k1), latex(k2)))

        # Các phương án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào danh sách và ngẫu nhiên thứ tự
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Lời giải chi tiết
        loigiai = ('''Áp dụng định lý Menelaus đối với tam giác $AND$ và cát tuyến $IGM$ ta có: \\\\
    $\\frac{MA}{MD} \\cdot \\frac{GD}{GN} \\cdot \\frac{IN}{IA} = 1 \\Leftrightarrow %s \\cdot %s \\cdot \\frac{IN}{IA} = 1 \\Leftrightarrow \\frac{IN}{IA} = \\frac{1}{%s} \\Leftrightarrow \\frac{AN}{NI} = %s$.'''
                   % (latex(k1), latex(k2), latex(k_prod), latex(kq_val)))
    dapan='\\shortans[0]{$%s$}\n'%(latex(kq_val))
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
        '\\loigiai{'+str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content  

