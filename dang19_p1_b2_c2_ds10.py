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


def bt_dang19_p1_b2_c2_ds10(self):
            # Định nghĩa hàm
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random tổng ngân sách (đơn vị: vạn)
                t = random.choice([500, 600, 700, 800, 900, 1000])

                # Random giá giống bưởi và xoài (đơn vị: vạn), đảm bảo c1 khác c2
                c1 = random.choice([21, 23, 25, 27, 29])
                c2 = random.choice([15, 17, 19, 22, 24])

                # Định dạng hiển thị chuỗi số tiền có dấu chấm phân cách hàng nghìn
                t_str = f"{t * 10000:,}".replace(",", ".")
                c1_str = f"{c1 * 10000:,}".replace(",", ".")
                c2_str = f"{c2 * 10000:,}".replace(",", ".")

                t_full = t * 10000
                c1_full = c1 * 10000
                c2_full = c2 * 10000

                # Các cấu trúc hệ bất phương trình
                he_dung = '\\begin{cases} x \\ge 0 \\\\ y \\ge 0 \\\\ %sx + %sy \\le %s \\end{cases}' % (c1, c2, t)
                he_sai1 = '\\begin{cases} x \\ge 0 \\\\ y \\ge 0 \\\\ %sx + %sy < %s \\end{cases}' % (c1, c2, t)
                he_sai2 = '\\begin{cases} x \\ge 0 \\\\ y \\ge 0 \\\\ %sx + %sy \\le %s \\end{cases}' % (c2, c1, t)
                he_sai3 = '\\begin{cases} x \\ge 0 \\\\ y \\ge 0 \\\\ %sx + %sy \\ge %s \\end{cases}' % (c1, c2, t)

                # Các đáp án trắc nghiệm
                da = '$%s$' % he_dung
                das1 = '$%s$' % he_sai1
                das2 = '$%s$' % he_sai2
                das3 = '$%s$' % he_sai3

                # Câu hỏi
                noidungcauhoi = ('''Một người nông dân dự định quy hoạch $x$ sào đất trồng cây Bưởi và $y$ sào đất trồng cây Xoài. Biết rằng người nông dân chỉ có tối đa $%s$đ mua giống và giá tiền mua giống cho mỗi sào đất trồng Bưởi là $%s$đ, mỗi sào đất trồng Xoài là $%s$đ. Trong các hệ bất phương trình sau, hệ bất phương trình nào mô tả các ràng buộc của $x$ và $y$?'''
                                 %(t_str, c1_str, c2_str))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Số tiền mua cây giống cho $x$ sào đất trồng Bưởi là: $%sx$ \\\\
                              Số tiền mua cây giống cho $y$ sào đất trồng Xoài là: $%sy$. \\\\
                              Biết rằng người nông dân chỉ có tối đa $%s$đ mua giống nên ta có bất phương trình:
                              $$%sx + %sy \\le %s \\Leftrightarrow %sx + %sy \\le %s.$$'''
                           %(c1_full, c2_full, t_str, c1_full, c2_full, t_full, c1, c2, t))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                       '\\choice \n'
                       '{'+str(list_1[0])+'}\n'
                       '{'+str(list_1[1])+'}\n'
                       '{'+str(list_1[2])+'}\n'
                       '{'+str(list_1[3])+'}\n'
                       '\\loigiai{'+str(loigiai)+'}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

