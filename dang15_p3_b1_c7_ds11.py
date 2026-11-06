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


def bt_dang15_p3_b1_c7_ds11(self):
            # Khai báo biến
            # B1 & B3: Thiết lập thông số và Random bài toán
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Khai báo biến t để tính toán sympy nếu cần, 
                # tuy nhiên bài này tính đại số cơ bản để tối ưu tốc độ.

                # Random hệ số phương trình s(t) = t^2 + b*t + c
                b = random.randint(2, 10)
                c = random.randint(1, 20)
                t0 = random.randint(3, 8)

                # Tính s(t0)
                st0 = t0**2 + b*t0 + c

                # Tính vận tốc v(t0) = s'(t0) = 2*t0 + b
                v_t0 = 2 * t0 + b

                # Giá trị hằng số trong giới hạn sau khi rút gọn: (t + t0 + b)
                const_lim = t0 + b

                # Giá trị tử số sau khi trừ: t^2 + b*t + (c - st0)
                tu_so_rut_gon = c - st0 # Số này luôn âm

                # Đáp án đúng
                kq = v_t0
                da = '$%s$' % (str(kq).replace('.', ','))

                # B4: Điều chỉnh phương án sai không trùng đáp án đúng
                s_options = set()
                while len(s_options) < 3:
                    sai = v_t0 + random.choice([-3, -2, -1, 1, 2, 3, 5])
                    if sai != v_t0 and sai > 0:
                        s_options.add('$%s$' % (str(sai).replace('.', ',')))

                list_sai = list(s_options)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # B2: Viết lại nội dung theo mẫu
                # Câu hỏi
                noidungcauhoi = (
                    'Một chất điểm chuyển động có phương trình chuyển động là: $s\\left(t\\right) = t^2 + %st + %s$ ($t$ được tính bằng giây, $s$ được tính bằng mét). Vận tốc tức thời của chuyển động tại thời điểm $t = %s$ bằng bao nhiêu?'
                    % (latex(b), latex(c), latex(t0))
                )

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = (
                    'Vận tốc tức thời của chuyển động tại thời điểm $t = %s$ là: \\\\ '
                    '$v\\left(%s\\right) = s\'\\left(%s\\right) = \\lim_{t \\to %s} \\frac{s\\left(t\\right) - s\\left(%s\\right)}{t - %s}$ \\\\ '
                    '$= \\lim_{t \\to %s} \\frac{t^2 + %st + %s - %s}{t - %s} = \\lim_{t \\to %s} \\frac{t^2 + %st %s}{t - %s}$ \\\\ '
                    '$= \\lim_{t \\to %s} \\left(t + %s\\right) = %s \\text{ (m/s)}.$'
                    % (
                        latex(t0), latex(t0), latex(t0), latex(t0), latex(t0), latex(t0),
                        latex(t0), latex(b), latex(c), latex(st0), latex(t0),
                        latex(t0), latex(b), latex(tu_so_rut_gon), latex(t0),
                        latex(t0), latex(const_lim), latex(v_t0)
                    )
                )
                dapan='\\shortans[0]{$%s$}\n'%(v_t0)
            # Xuất câu trắc nghiệm theo cấu trúc yêu cầu
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content      

