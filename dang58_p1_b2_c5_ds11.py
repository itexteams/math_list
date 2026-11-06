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


def bt_dang58_p1_b2_c5_ds11(self):
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random hệ số n2 để tạo căn bậc n cho cơ số log
                n2 = random.randint(2, 4)
                n3 = 2 * n2 - 1

                # Random các hệ số A, B, C trong biểu thức P = A(x/y) + B(y/z) + C(z/x)
                A = random.randint(2, 15)
                B = random.randint(1, 10)
                C = random.randint(2, 12)

                # Vì x = y = z nên P = A + B + C
                kq_val = A + B + C
                da_dung = '$%s$' % (latex(kq_val))

                # --- BƯỚC 4: TẠO PHƯƠNG ÁN SAI (KHÔNG TRÙNG ĐÁP ÁN ĐÚNG) ---
                s = []
                while len(s) < 3:
                    sai = kq_val + random.choice([-3, -2, -1, 1, 2, 3, 5, 10])
                    if sai != kq_val and sai > 0 and str(sai) not in s:
                        s.append('$%s$' % (latex(sai)))

                # Thiết lập cách hiển thị căn bậc cho latex
                base_y = "\\sqrt{a}" if n2 == 2 else "\\sqrt[%s]{a}" % n2
                base_z = "\\sqrt[%s]{a}" % n3

                # Nội dung câu hỏi
                noidungcauhoi = (
                    r"Cho $x, y, z$ là ba số thực dương lập thành cấp số nhân; "
                    r"$\log_{a} x, \log_{%s} y, \log_{%s} z$ lập thành cấp số cộng, với $a$ là số thực dương khác $1$. "
                    r"Giá trị của biểu thức $P = \frac{%sx}{y} + \frac{%sy}{z} + \frac{%sz}{x}$ là"
                    % (base_y, base_z, latex(A) if A != 1 else "", latex(B) if B != 1 else "", latex(C) if C != 1 else "")
                )

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                list_1 = [da_d, s[0], s[1], s[2]]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (
                    r"$x, y, z$ là ba số thực dương lập thành cấp số nhân nên ta có $xz = y^2$ (1).\\"
                    r"$\log_{a} x, \log_{%s} y, \log_{%s} z$ lập thành cấp số cộng nên:\\"
                    r"$\log_{a} x + \log_{%s} z = 2\log_{%s} y \Leftrightarrow \log_{a} x + %s\log_{a} z = %s\log_{a} y \Leftrightarrow xz^{%s} = y^{%s}$ (2).\\"
                    r"Từ (1) và (2) ta suy ra $x = y = z$.\\"
                    r"Vậy $P = \frac{%sx}{y} + \frac{%sy}{z} + \frac{%sz}{x} = %s + %s + %s = %s$."
                    % (base_y, base_z, base_z, base_y, n3, 2*n2, n3, 2*n2, 
                       latex(A) if A != 1 else "", latex(B) if B != 1 else "", latex(C) if C != 1 else "",
                       A, B, C, kq_val)
                )

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

