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


def bt_dang17_p3_b3_c2_hh11(self):
            # Khai báo biến
            # Để SB = sqrt(m^2 + p^2) là một số đẹp (số nguyên), ta có thể chọn các bộ số Pitago
            triples = [(3, 4), (4, 3), (5, 12), (12, 5), (8, 15), (15, 8)]
            m, p = random.choice(triples)

            a = symbols('a')
            AB_val = m * a
            SA_val = p * a
            SB_val = sqrt(m**2 + p**2) * a

            # Tính toán các đại lượng liên quan
            # AC là đường chéo hình vuông cạnh ma
            AC_sq = 2 * (m**2)
            AC_val = m * sqrt(2) * a

            # SC là cạnh huyền tam giác vuông SAC
            SC_sq = p**2 + AC_sq
            SC_val = sqrt(SC_sq) * a

            # Tính sin của góc giữa SC và mặt phẳng (ABCD) là góc SCA
            # sin(SCA) = SA / SC
            sin_val = simplify(p / sqrt(SC_sq))

            # Bước 4: Tạo các phương án sai không trùng với đáp án đúng
            kq_dung = '$%s$' % (latex(sin_val).replace('.', ','))

            # Phương án sai 1: Nhầm sang cos (AC/SC)
            da_s1_val = simplify(m * sqrt(2) / sqrt(SC_sq))
            # Phương án sai 2: Nhầm sang tan (SA/AC)
            da_s2_val = simplify(p / (m * sqrt(2)))
            # Phương án sai 3: Nhầm cạnh SB thay vì SC
            da_s3_val = simplify(p / sqrt(m**2 + p**2))

            da_s1 = '$%s$' % (latex(da_s1_val).replace('.', ','))
            da_s2 = '$%s$' % (latex(da_s2_val).replace('.', ','))
            da_s3 = '$%s$' % (latex(da_s3_val).replace('.', ','))

            # Đảm bảo không trùng lặp (dù xác suất rất thấp với bộ số này)
            choices_set = {kq_dung, da_s1, da_s2, da_s3}
            while len(choices_set) < 4:
                extra = '$%s$' % (latex(Rational(randint(1, 5), randint(6, 10)) * sqrt(randint(2, 5))).replace('.', ','))
                choices_set.add(extra)

            list_choices = list(choices_set)
            # Tìm lại vị trí đáp án đúng để gán \True
            for i in range(len(list_choices)):
                if list_choices[i] == kq_dung:
                    list_choices[i] = '\\True ' + list_choices[i]

            random.shuffle(list_choices)

            # Hình vẽ TikZ
            tikz_pic = (
                '\\begin{center}\n'
                '\\begin{tikzpicture}[line cap=round,line join=round, scale=0.8, line width=1pt]\n'
                '\\coordinate (A) at (0,3);\n'
                '\\coordinate (B) at (-1.5,1.5);\n'
                '\\coordinate (C) at (2.5,1.5);\n'
                '\\coordinate (D) at (4,3);\n'
                '\\coordinate (S) at (0,7);\n'
                '\\coordinate (O) at (1.25, 2.25);\n'
                '\\draw [dashed] (S)--(A)--(B) (A)--(D) (A)--(C) (B)--(D);\n'
                '\\draw (S)--(B)--(C)--(D)--cycle (S)--(C);\n'
                '\\draw (A) node[left] {$A$} (B) node[left] {$B$} (C) node[below right] {$C$} (D) node[right] {$D$} (S) node[above] {$S$} (O) node[below] {$O$};\n'
                '\\tkzMarkRightAngle[size=0.3](S,A,B)\n'
                '\\tkzMarkRightAngle[size=0.3](S,A,D)\n'
                '\\draw (2,1.5) arc (180:140:0.5);\n'
                '\\end{tikzpicture}\n'
                '\\end{center}'
            )

            # Bước 2: Viết nội dung câu hỏi và lời giải chi tiết
            noidungcauhoi = (
                'Cho hình chóp $S.ABCD$ có đáy là hình vuông cạnh $%s$, $SA$ vuông góc với mặt phẳng đáy, '
                '$SB = %s$. $\\sin$ của góc giữa $SC$ và mặt phẳng $\\left( ABCD \\right)$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).'
                % (latex(AB_val), latex(SB_val))
            )
            h1=sin_val
            number = Decimal(float(h1))  # Số cần làm tròn
            kq1 = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            kqz=str(kq1).replace('.', ',')
            loigiai = (
                'ABCD là hình vuông cạnh $%s$ nên $AC = %s \\cdot \\sqrt{2} = %s$.\\\\\n'
                'Xét tam giác $SAB$ vuông tại $A$: $SA = \\sqrt{SB^2 - AB^2} = \\sqrt{\\left( %s \\right)^2 - \\left( %s \\right)^2} = %s$.\\\\\n'
                'Vì $SA \\perp \\left( ABCD \\right)$ nên hình chiếu của $SC$ lên mặt phẳng $\\left( ABCD \\right)$ là $AC$.\\\\\n'
                'Suy ra $\\left( SC, \\left( ABCD \\right) \\right) = \\widehat{SCA}$.\\\\\n'
                'Xét tam giác $SAC$ vuông tại $A$:\\\\\n'
                '$SC = \\sqrt{SA^2 + AC^2} = \\sqrt{\\left( %s \\right)^2 + \\left( %s \\right)^2} = %s$.\\\\\n'
                '$\\sin \\widehat{SCA} = \\frac{SA}{SC} = \\frac{%s}{%s} = %s \\approx %s$.'
                % (latex(AB_val), latex(m*a), latex(AC_val), 
                   latex(SB_val), latex(AB_val), latex(SA_val),
                   latex(SA_val), latex(AC_val), latex(SC_val),
                   latex(SA_val), latex(SC_val), latex(sin_val).replace('.', ','),kqz)
            )
            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(latex(kqz))

            # Xuất nội dung theo định dạng mẫu
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + tikz_pic+ str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

