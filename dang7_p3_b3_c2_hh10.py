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


def bt_dang7_p3_b3_c2_hh10(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':

        k = randint(1, 3)
        val_AB = 3 * k
        val_CD = 9 * k
        val_AD = 6 * k


        x_I = Rational(val_AB + 2 * val_CD, 4)
        y_I = Rational(val_AD, 2)


        p_min = val_AB + 2 * val_CD

        # Làm tròn/định dạng kết quả theo quy tắc
        number = Decimal(str(p_min))
        kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình thang $ABCD$ vuông tại $A$ và $D$ có $AB = %s$, $CD = %s$ và $AD = %s$. Điểm $M$ di động trên đoạn thẳng $AD$. Giá trị nhỏ nhất của biểu thức $P = \\left| \\vec{MA} + \\vec{MB} + 2\\vec{MC} \\right|$ bằng bao nhiêu?'''
                         % (latex(val_AB), latex(val_CD), latex(val_AD)))

        # Nội dung lời giải
        loigiai = ('''Gọi $I$ là điểm thỏa mãn $\\vec{IA} + \\vec{IB} + 2\\vec{IC} = \\vec{0}$. \\\\
    Khi đó với mọi điểm $M$, ta có: \\\\
    $\\vec{MA} + \\vec{MB} + 2\\vec{MC} = (\\vec{MI} + \\vec{IA}) + (\\vec{MI} + \\vec{IB}) + 2(\\vec{MI} + \\vec{IC}) = 4\\vec{MI} + (\\vec{IA} + \\vec{IB} + 2\\vec{IC}) = 4\\vec{MI}$. \\\\
    Suy ra $P = \\left| \\vec{MA} + \\vec{MB} + 2\\vec{MC} \\right| = 4MI$. \\\\
    Chọn hệ trục tọa độ $Oxy$ sao cho gốc tọa độ trùng với $D$, tia $Dx$ chứa cạnh $DC$ và tia $Dy$ chứa cạnh $DA$. \\\\
    Tọa độ các đỉnh là: $D(0;0)$, $A(0;%s)$, $B(%s;%s)$, $C(%s;0)$. \\\\
    Gọi $I(x_I; y_I)$. Từ đẳng thức $\\vec{IA} + \\vec{IB} + 2\\vec{IC} = \\vec{0}$, ta có: \\\\
    $\\begin{cases} (0 - x_I) + (%s - x_I) + 2(%s - x_I) = 0 \\\\ (%s - y_I) + (%s - y_I) + 2(0 - y_I) = 0 \\end{cases} \\Leftrightarrow \\begin{cases} 4x_I = %s \\\\ 4y_I = %s \\end{cases} \\Leftrightarrow \\begin{cases} x_I = %s \\\\ y_I = %s \\end{cases}$ \\\\
    Suy ra $I\\left(%s; %s\\right)$. \\\\
    Vì $M$ thuộc đoạn thẳng $AD$ nằm trên trục tung nên $M(0; y_M)$ với $0 \\le y_M \\le %s$. \\\\
    Độ dài đoạn thẳng $MI$ là: \\\\
    $MI = \\sqrt{(x_I - 0)^2 + (y_I - y_M)^2} = \\sqrt{\\left(%s\\right)^2 + \\left(%s - y_M\\right)^2} \\ge %s$. \\\\
    Dấu đẳng thức xảy ra khi $y_M = %s$ (thỏa mãn $0 \\le %s \\le %s$). \\\\
    Vậy giá trị nhỏ nhất của $P$ là $P_{\\min} = 4 \\cdot %s = %s$.'''
                   % (latex(val_AD), latex(val_AB), latex(val_AD), latex(val_CD),
                      latex(val_AB), latex(val_CD),
                      latex(val_AD), latex(val_AD),
                      latex(val_AB + 2 * val_CD), latex(2 * val_AD),
                      latex(x_I), latex(y_I),
                      latex(x_I), latex(y_I),
                      latex(val_AD),
                      latex(x_I), latex(y_I), latex(x_I),
                      latex(y_I), latex(y_I), latex(val_AD),
                      latex(x_I), str(kq_str)))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n' +
               '\\end{minipage} \n\n')
    return content

