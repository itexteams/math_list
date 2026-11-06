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


def bt_dang45_p3_b2_c1_ds10(self):
            # Khai báo các tham số
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 1: Chọn số trang ngẫu nhiên (từ 100 đến 500 để đảm bảo có 3 chữ số)
                n = randint(120, 450)

                # Bước 2: Tính toán số chữ số
                # Từ 1 đến 9: 9 trang, mỗi trang 1 chữ số
                s1 = 9 * 1
                # Từ 10 đến 99: 90 trang, mỗi trang 2 chữ số
                s2 = 90 * 2
                # Từ 100 đến n: (n - 100 + 1) trang, mỗi trang 3 chữ số
                so_trang_3_chu_so = n - 99
                s3 = so_trang_3_chu_so * 3

                # Tổng số chữ số
                ket_qua = s1 + s2 + s3

                # Bước 3: Tạo các phương án sai
                s = [
                    '$%s$'%(latex(ket_qua + 1)),
                    '$%s$'%(latex(ket_qua - 1)),
                    '$%s$'%(latex(ket_qua + 2)),
                    '$%s$'%(latex(ket_qua - 2)),
                    '$%s$'%(latex(ket_qua + 10)),
                    '$%s$'%(latex(ket_qua - 10)),
                ]

                # Chọn ngẫu nhiên 3 đáp án sai từ danh sách và loại bỏ trùng lặp nếu có
                s = list(set(s))
                if str('$%s$'%(latex(ket_qua))) in s:
                    s.remove('$%s$'%(latex(ket_qua)))

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Nội dung câu hỏi
                noidungcauhoi = ('Một quyển sách có $%s$ trang được đánh số từ $1$ đến $%s$. Số các chữ số dùng để đánh số trang của quyển sách này bằng bao nhiêu?'
                                 %(latex(n), latex(n)))

                # Đáp án đúng
                da_d = ('\\True $%s$' % (latex(ket_qua)))

                # Đưa các đáp án vào danh sách và xáo trộn
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Để đánh số trang của quyển sách từ trang $1$ đến trang $%s$, ta chia thành các nhóm sau: \\\\
                             - Từ trang $1$ đến trang $9$: có $9$ trang. Số chữ số cần dùng là $9 \\cdot 1 = 9$ (chữ số). \\\\
                             - Từ trang $10$ đến trang $99$: có $99 - 10 + 1 = 90$ trang. Số chữ số cần dùng là $90 \\cdot 2 = 180$ (chữ số). \\\\
                             - Từ trang $100$ đến trang $%s$: có $%s - 100 + 1 = %s$ trang. Số chữ số cần dùng là $%s \\cdot 3 = %s$ (chữ số). \\\\
                             Vậy tổng số các chữ số dùng để đánh số trang của quyển sách này là: \\\\
                             $9 + 180 + %s = %s$ (chữ số).'''
                           %(latex(n), 
                             latex(n), latex(n), latex(so_trang_3_chu_so), 
                             latex(so_trang_3_chu_so), latex(s3),
                             latex(s3), latex(ket_qua)
                            ))
                dapan='\\shortans[0]{$%s$}\n'%(latex(ket_qua))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

