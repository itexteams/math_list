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


def bt_dang14_p4_b3_c2_hh11(self):
            # Khai báo biến
            # Mỗi kịch bản: (Giá trị AB_tex, Giá trị SB_tex, Đáp án đúng_tex, cos_value_tex)
            scenarios = [
                ('a', '2a', '60^\\circ', '\\frac{a}{2a} = \\frac{1}{2}'),
                ('a', 'a\\sqrt{2}', '45^\\circ', '\\frac{a}{a\\sqrt{2}} = \\frac{\\sqrt{2}}{2}'),
                ('a\\sqrt{3}', '2a', '30^\\circ', '\\frac{a\\sqrt{3}}{2a} = \\frac{\\sqrt{3}}{2}')
            ]

            # Chọn ngẫu nhiên một kịch bản
            sel_ab, sel_sb, correct_angle, cos_step = random.choice(scenarios)

            # Các phương án nhiễu
            all_angles = ['30^\\circ', '45^\\circ', '60^\\circ', '90^\\circ']
            if correct_angle in all_angles:
                all_angles.remove(correct_angle)
            random.shuffle(all_angles)

            da_d = ('\\True $' + correct_angle + '$')
            da_s1 = '$' + all_angles[0] + '$'
            da_s2 = '$' + all_angles[1] + '$'
            da_s3 = '$' + all_angles[2] + '$'

            # Trộn đáp án
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung câu hỏi
            noidungcauhoi = (
                'Cho hình chóp $S.ABC$ có $SA$ vuông góc với mặt phẳng đáy, $AB = ' + sel_ab + '$ và $SB = ' + sel_sb + '$. '
                'Tính góc giữa đường thẳng $SB$ và mặt phẳng đáy.'
            )

            # Vẽ hình bằng TikZ
            ve_hinh = (
                '\\begin{center}\n'
                '\\begin{tikzpicture}[scale=1, line join=round, line cap=round, line width=1pt]\n'
                '   \\coordinate (A) at (0,0);\n'
                '   \\coordinate (B) at (3.5,0);\n'
                '   \\coordinate (C) at (1.2,-1.2);\n'
                '   \\coordinate (S) at (0,3.5);\n'
                '   \\draw (S)--(A) (S)--(B) (S)--(C) (B)--(C) (A)--(C);\n'
                '   \\draw[dashed] (A)--(B) ;\n'
                '   \\draw (0,0.3)--(0.3,0.3)--(0.3,0);\n'
                '   \\node at (A) [left] {$A$};\n'
                '   \\node at (B) [right] {$B$};\n'
                '   \\node at (C) [below] {$C$};\n'
                '   \\node at (S) [above] {$S$};\n'
                '   \\node at (1.8,0.3) [above] {$' + sel_ab + '$};\n'
                '   \\node at (1.8,2) [right] {$' + sel_sb + '$};\n'
                '\\end{tikzpicture}\n'
                '\\end{center}'
            )

            # Lời giải chi tiết
            loigiai = (
                'Ta có $SA \\perp (ABC)$ tại $A$ nên $AB$ là hình chiếu vuông góc của $SB$ lên mặt phẳng đáy $(ABC)$.\\\\ \n'
                '        Suy ra góc giữa đường thẳng $SB$ và mặt phẳng đáy là góc giữa $SB$ và $AB$, chính là góc $\\widehat{SBA}$.\\\\ \n'
                '        Tam giác $SAB$ vuông tại $A$ (do $SA \\perp AB$), ta có: \n'
                '        $$\\cos \\widehat{SBA} = \\frac{AB}{SB} = ' + cos_step + '$$\n'
                '        Do đó $\\widehat{SBA} = ' + correct_angle + '$.'
            )

            # Xuất nội dung theo cấu trúc mẫu
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + noidungcauhoi + '\n'
                '\\loigiai{' + ve_hinh + loigiai + '}\n'
                '\\end{ex}\n'
                '\\end{minipage} \n\n')
            return content

