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


def bt_dang30_p4_b3_c2_hh11(self):
            # Khai báo biến
            # Dạng 2: Tam giác SBC vuông cân tại S -> Góc là 30 độ

            lisdang = ['1', '2']
            dang = random.choice(lisdang)

            if dang == '1':
                loai_tam_giac = 'đều'
                ket_qua = '45^\\circ'
                ti_so = '1'
                cach_tinh_sh = 'SH = \\frac{a\\sqrt{3}}{2}'
                s_s1, s_s2, s_s3 = '30^\\circ', '60^\\circ', '90^\\circ'
            else:
                loai_tam_giac = 'vuông cân tại $S$'
                ket_qua = '30^\\circ'
                ti_so = '\\frac{1}{\\sqrt{3}}'
                cach_tinh_sh = 'SH = \\frac{a}{2}'
                s_s1, s_s2, s_s3 = '45^\\circ', '60^\\circ', '15^\\circ'

            # B2: Nội dung câu hỏi
            noidungcauhoi = (
                'Cho hình chóp $S.ABC$ có đáy là tam giác đều cạnh $a$. Hình chiếu vuông góc của $S$ lên mặt phẳng $\\left( ABC \\right)$ là trung điểm $H$ của cạnh $BC$. Biết tam giác $SBC$ %s, tính góc giữa đường thẳng $SA$ và mặt phẳng $\\left( ABC \\right)$.'
                % (loai_tam_giac)
            )

            # Các đáp án
            da_d = '\\True $' + ket_qua + '$'
            da_s1 = '$' + s_s1 + '$'
            da_s2 = '$' + s_s2 + '$'
            da_s3 = '$' + s_s3 + '$'

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Hình vẽ TikZ
            hinh_ve = (
                '\\begin{center}\n'
                '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
                '\\coordinate (H) at (0,0);\n'
                '\\coordinate (B) at (-1.5,-0.6);\n'
                '\\coordinate (C) at (1.5,0.6);\n'
                '\\coordinate (S) at (0,3.5);\n'
                '\\coordinate (A) at (4,0);\n'
                '\\draw [line width=1pt] (S)--(B)  (S)--(A) (A)--(B) ;\n'
                '\\draw [dashed, line width=1pt] (B)--(C) (S)--(C) (A)--(C) (A)--(H) (S)--(H);\n'
                '\\node [above] at (S) {$S$};\n'
                '\\node [left] at (B) {$B$};\n'
                '\\node [right] at (C) {$C$};\n'
                '\\node [right] at (A) {$A$};\n'
                '\\node [below left] at (H) {$H$};\n'
                '\\draw [line width=0.6pt] (0.2,0) -- (0.2,0.2) -- (0,0.2);\n'
                '\\tkzMarkAngle[size=0.6, line width=0.8pt](S,A,H)\n'
                '\\end{tikzpicture}\n'
                '\\end{center}'
            )

            # Lời giải chi tiết
            loigiai = (
                'Gọi $H$ là trung điểm của $BC$. Theo giả thiết, $SH \\perp \\left( ABC \\right)$. \\\\'
                'Khi đó, hình chiếu vuông góc của đường thẳng $SA$ trên mặt phẳng $\\left( ABC \\right)$ là đường thẳng $AH$. \\\\'
                'Suy ra góc giữa $SA$ và mặt phẳng $\\left( ABC \\right)$ là góc $\\widehat{SAH}$. \\\\'
                'Tam giác $ABC$ đều cạnh $a$ nên chiều cao $AH = \\frac{a\\sqrt{3}}{2}$. \\\\'
                'Xét tam giác $SBC$ %s cạnh $BC = a$, ta có đường cao $%s$. \\\\'
                'Xét tam giác $SAH$ vuông tại $H$, ta có: \\\\'
                '$\\tan \\widehat{SAH} = \\frac{SH}{AH} = \\frac{%s}{%s} = %s$. \\\\'
                'Vậy $\\widehat{SAH} = %s$.'
                % (loai_tam_giac, cach_tinh_sh, cach_tinh_sh.split('=')[1].strip(), 'a\\sqrt{3}/2', ti_so, ket_qua)
            )

            # B4: Xuất nội dung theo cấu trúc yêu cầu
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'
                + str(noidungcauhoi) + '\n'
                '\\loigiai{' + hinh_ve+ str(loigiai) + '}\n'
                '\\end{ex}\n'
                '\\end{minipage} \n\n')
            return content

