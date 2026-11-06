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


def bt_dang41_p4_b1_c2_hh11(self):
            # Khai báo biến
            # Trong bài mẫu: SC = 2, a = 4*sqrt(2).
            list_h = [2, 4, 6] 
            h_val = random.choice(list_h) # h_val tương ứng với đoạn SC
            a_factor = 2 * h_val # Hệ số của sqrt(2) cho cạnh a

            # Các đại lượng tính toán (dưới dạng biểu thức Sympy để xuất LaTeX đẹp)
            a = a_factor * sqrt(2)
            SC = h_val
            CN = a / 2 # = h_val * sqrt(2)
            SN_sq = SC**2 + CN**2 # = h^2 + 2h^2 = 3h^2
            SN = sqrt(SN_sq) # = h*sqrt(3)

            # CM là đường cao tam giác đều: a*sqrt(3)/2
            CM = (a * sqrt(3)) / 2 
            NI = CM / 2
            NI_sq = NI**2

            # Tính CI trong tam giác vuông CMI (tại M)
            # MI = 1/4 * a
            MI = a / 4
            CI_sq = CM**2 + MI**2
            CI = sqrt(CI_sq)

            # SI trong tam giác vuông SCI (tại C)
            SI_sq = SC**2 + CI_sq
            SI = sqrt(SI_sq)

            # Tính cos(SNI) theo định lý cosin trong tam giác SNI
            # cos = (SN^2 + NI^2 - SI^2) / (2 * SN * NI)
            tu_so = SN_sq + NI_sq - SI_sq
            mau_so = 2 * SN * NI
            cos_val = tu_so / mau_so # Sẽ ra -sqrt(2)/2

            # Đáp án
            da_dung = '45^\\circ'
            list_sai = ['30^\\circ', '60^\\circ', '90^\\circ', '120^\\circ']
            random.shuffle(list_sai)
            das1, das2, das3 = list_sai[:3]

            # Nội dung câu hỏi
            noidungcauhoi = (
                'Cho hình chóp $S.ABC$ có đáy là tam giác đều cạnh $a = %s\\text{cm}$, cạnh bên $SC$ vuông góc với đáy và $SC = %s\\text{cm}$. '
                'Gọi $M, N$ là trung điểm của $AB$ và $BC$. Tính góc giữa hai đường thẳng $SN$ và $CM$.'
                % (latex(a), latex(SC))
            )

            # Nội dung lời giải
            loigiai = (    '\\begin{center}\n'
                '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round]\n'
                '\\coordinate (C) at (0,0);\n'
                '\\coordinate (A) at (4,-1);\n'
                '\\coordinate (B) at (1.5,-2.5);\n'
                '\\coordinate (S) at (0,4);\n'
                '\\coordinate (N) at ($(C)!0.5!(B)$);\n'
                '\\coordinate (M) at ($(A)!0.5!(B)$);\n'
                '\\coordinate (I) at ($(B)!0.5!(M)$);\n'
                '\\draw (S)--(C)--(B)--(A)--(S)--(B);\n'
                '\\draw (S)--(N);\n'
                '\\draw  (S)--(I);\n'
                '\\draw[dashed] (C)--(A) (C)--(M) (N)--(I) (C)--(I);\n'
                '\\foreach \\p/\\pos in {S/above, C/left, A/right, B/below, N/left, M/right, I/below}\n'
                '\\fill (\\p) node[\\pos] {$\\p$};\n'
                '\\end{tikzpicture}\n'
                '\\end{center}\n'
                'Gọi $I$ là trung điểm của $BM$, ta có $NI \\parallel CM$ (do $NI$ là đường trung bình tam giác $BCM$) '
                'nên góc giữa $SN$ và $CM$ là góc giữa $SN$ và $NI$.\\\\ '
                'Xét tam giác $SNI$ có:\\\\ '
                '$SN = \\sqrt{SC^2 + CN^2} = \\sqrt{%s^2 + (%s)^2} = %s$;\\\\ '
                '$NI = \\frac{1}{2} CM = \\frac{1}{2} \\cdot \\frac{%s \\cdot \\sqrt{3}}{2} = %s$;\\\\ '
                '$CI = \\sqrt{CM^2 + MI^2} = \\sqrt{(%s)^2 + (%s)^2} = %s \\Rightarrow SI = \\sqrt{SC^2 + CI^2} = \\sqrt{%s^2 + (%s)^2} = %s$.\\\\ '
                'Vậy $\\cos \\widehat{SNI} = \\frac{SN^2 + NI^2 - SI^2}{2 \\cdot SN \\cdot NI} = \\frac{%s + %s - %s}{2 \\cdot %s \\cdot %s} = %s \\Rightarrow \\widehat{SNI} = 135^\\circ$.\\\\ '
                'Vì góc giữa hai đường thẳng luôn $\\le 90^\\circ$ nên góc giữa $SN$ và $CM$ bằng $180^\\circ - 135^\\circ = 45^\\circ$.'
                % (latex(SC), latex(CN), latex(SN), 
                   latex(a), latex(NI), 
                   latex(CM), latex(MI), latex(CI), latex(SC), latex(CI), latex(SI),
                   latex(SN_sq), latex(NI_sq), latex(SI_sq), latex(SN), latex(NI), latex(cos_val))
            )

            # Sắp xếp đáp án
            list_ans = ['\\True $' + da_dung + '$', '$' + das1 + '$', '$' + das2 + '$', '$' + das3 + '$']
            random.shuffle(list_ans)

            # Xuất nội dung theo định dạng yêu cầu
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + noidungcauhoi + '\n'
                '\\loigiai{' + loigiai + '}\n'
                '\\end{ex}\n'
                '\\end{minipage} \n\n')
            return content

