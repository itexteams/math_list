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


def bt_dang10_p4_b6_c2_hh11(self):
            # Khai báo biến
            # SA = n*a, AB = m*a. Trong ảnh n=1, m=2.
            n = random.randint(1, 4)
            m = random.randint(2, 6)
            a = symbols('a')

            # Tính toán diện tích đáy và thể tích
            # Diện tích tam giác vuông cân tại A: S = 1/2 * AB * AC = 1/2 * (m*a)^2
            s_day_val = Rational(m**2, 2)
            s_day_latex = latex(s_day_val) + 'a^2'

            # Thể tích: V = 1/3 * SA * S_day = 1/3 * (n*a) * (m^2/2 * a^2) = (n*m^2)/6 * a^3
            v_num = n * m**2
            v_den = 6
            v_val = Rational(v_num, v_den)

            # Đáp án đúng
            da_dung = '$V = %s a^3$' % (latex(v_val))

            # B4: Tạo các phương án sai (đảm bảo không trùng)
            s = set()
            wrong_candidates = [
                Rational(v_num, 2),  # Quên 1/3
                Rational(v_num, 3),  # Quên 1/2
                Rational(v_num, 12), # Nhầm công thức
                Rational(v_num, 18), 
                v_val * 2,
                v_val / 2
            ]

            for cand in wrong_candidates:
                if cand != v_val:
                    s.add('$V = %s a^3$' % (latex(cand)))

            list_sai = list(s)
            random.shuffle(list_sai)

            das1 = list_sai[0]
            das2 = list_sai[1]
            das3 = list_sai[2]

            # Nội dung câu hỏi
            noidungcauhoi = (
                'Cho hình chóp $S.ABC$ có cạnh bên $SA$ vuông góc với mặt phẳng đáy $(ABC)$. Biết $SA = %sa$, '
                'tam giác $ABC$ là tam giác vuông cân tại $A$, $AB = %sa$. Tính thể tích $V$ khối chóp $S.ABC$.'
                % ('' if n == 1 else latex(n), latex(m))
            )



            # Lời giải chi tiết (B2)
            # Thay thế dấu chấm thập phân bằng dấu phẩy nếu có (ở đây dùng phân số nên ít gặp)
            loigiai = (
                'Diện tích tam giác $ABC$ vuông cân tại $A$ là: $S_{ABC} = \\frac{1}{2} AB \\cdot AC = '
                '\\frac{1}{2} \\cdot %sa \\cdot %sa = %s a^2$. \\\\\n'
                'Thể tích khối chóp $S.ABC$ là: $V_{S.ABC} = \\frac{1}{3} SA \\cdot S_{ABC} = '
                '\\frac{1}{3} \\cdot %sa \\cdot %s a^2 = %s a^3$.'
                % (latex(m), latex(m), latex(s_day_val), latex(n), latex(s_day_val), latex(v_val))
            ).replace('.', ',')

            # Trộn đáp án
            da_d = '\\True ' + da_dung
            list_1 = [da_d, das1, das2, das3]
            random.shuffle(list_1)

            # Xuất nội dung
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

