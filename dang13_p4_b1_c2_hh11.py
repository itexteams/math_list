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


def bt_dang13_p4_b1_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random cạnh của tứ diện đều là k*a
                # Nếu k=1 thì giống hệt đề bài trong ảnh
                k = randint(1, 6)

                if k == 1:
                    canh_hien_thi = 'a'
                    canh_binh_phuong_latex = 'a^2'
                else:
                    canh_hien_thi = str(k) + 'a'
                    canh_binh_phuong_latex = str(k**2) + 'a^2'

                # Tính toán giá trị đúng: k^2 * a^2 + (k^2 * a^2)/2 = 3/2 * k^2 * a^2
                tu_so_dung = 3 * k**2
                mau_so_dung = 2

                # Rút gọn phân số cho đáp án đúng
                kq_dung = Rational(tu_so_dung, mau_so_dung)
                da_dung_str = '$%s a^2$' % (latex(kq_dung))

                # Tạo các đáp án sai dựa trên cấu trúc các phương án A, B, C trong ảnh
                # Sai 1: a^2/2 -> (k^2/2)a^2
                kq_sai1 = Rational(k**2, 2)
                das1 = '$%s a^2$' % (latex(kq_sai1))

                # Sai 2: (a^2*sqrt(2))/2 -> (k^2*sqrt(2)/2)a^2
                das2 = '$\\frac{%s\\sqrt{2}}{2} a^2$' % (latex(k**2) if k > 1 else '')

                # Sai 3: (a^2*sqrt(3))/2 -> (k^2*sqrt(3)/2)a^2
                das3 = '$\\frac{%s\\sqrt{3}}{2} a^2$' % (latex(k**2) if k > 1 else '')

                # Câu hỏi
                noidungcauhoi = ('''Cho tứ diện đều $ABCD$ có cạnh bằng $%s$. Tính $\\vec{AB}(\\vec{AB}-\\vec{CA})$.'''
                                 %(canh_hien_thi))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung_str))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết theo hình ảnh
                # Lưu ý: -CA_vector = AC_vector
                loigiai=('''Ta có: $\\vec{AB}(\\vec{AB}-\\vec{CA}) = \\vec{AB} \\cdot \\vec{AB} + \\vec{AB} \\cdot \\vec{AC} = \\vec{AB}^2 + |\\vec{AB}| \\cdot |\\vec{AC}| \\cdot \\cos(\\vec{AB}, \\vec{AC})$ \\\\
                          $= AB^2 + AB \\cdot AC \\cdot \\cos(\\widehat{BAC}) = %s + %s \\cdot %s \\cdot \\cos 60^\\circ$ \\\\
                          $= %s + \\frac{%s}{2} =$ %s.'''
                         %(canh_binh_phuong_latex, canh_hien_thi, canh_hien_thi, 
                           canh_binh_phuong_latex, canh_binh_phuong_latex, da_dung_str))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

