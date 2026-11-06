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


def bt_dang14_p3_b3_c2_hh11(self):
            # Khai báo biến
            # =================================================================
            list_cases = [
                {
                    'mo_ta_canh': 'có tất cả các cạnh bằng $a$',
                    'kq_val': '45',
                    'ly_luan': 'AA\' = A\'B\' = a \\Rightarrow \\Delta AA\'B\' \\text{ vuông cân tại } A\''
                },
                {
                    'mo_ta_canh': 'có cạnh đáy bằng $a$ và cạnh bên bằng $a\\sqrt{3}$',
                    'kq_val': '60',
                    'ly_luan': '\\tan \\widehat{AB\'A\'} = \\frac{AA\'}{A\'B\'} = \\frac{a\\sqrt{3}}{a} = \\sqrt{3}'
                },
                {
                    'mo_ta_canh': 'có cạnh đáy bằng $a\\sqrt{3}$ và cạnh bên bằng $a$',
                    'kq_val': '30',
                    'ly_luan': '\\tan \\widehat{AB\'A\'} = \\frac{AA\'}{A\'B\'} = \\frac{a}{a\\sqrt{3}} = \\frac{1}{\\sqrt{3}}'
                }
            ]

            case = random.choice(list_cases)
            kq_str = case['kq_val'] + '^\\circ'

            # =================================================================
            # B4: Điều chỉnh các phương án sai không trùng đáp án đúng
            # =================================================================
            all_options = ['30^\\circ', '45^\\circ', '60^\\circ', '90^\\circ', '120^\\circ', '150^\\circ']
            # Loại bỏ đáp án đúng khỏi danh sách mồi nhử
            wrong_candidates = [opt for opt in all_options if opt != kq_str]
            random.shuffle(wrong_candidates)

            da_d = '\\True $' + kq_str + '$'
            da_s1 = '$' + wrong_candidates[0] + '$'
            da_s2 = '$' + wrong_candidates[1] + '$'
            da_s3 = '$' + wrong_candidates[2] + '$'

            list_ans = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_ans)

            # =================================================================
            # B2: Viết lại bài toán và lời giải (giữ nguyên định dạng mẫu)
            # =================================================================

            # Nội dung câu hỏi
            noidungcauhoi = (
                'Cho lăng trụ đứng $ABC.A\'B\'C\'$ ' + case['mo_ta_canh'] + '. '
                'Góc giữa đường thẳng $AB\'$ và mặt phẳng $(A\'B\'C\')$ bằng bao nhiêu?'
            )

            # Mã TikZ minh họa
            tikz_code = (
                '\\begin{center}\n'
                '\\begin{tikzpicture}[scale=1.5, line join=round, line cap=round, line width=1pt]\n'
                '   \\coordinate (A1) at (0,0); \\coordinate (B1) at (1,0.5); \\coordinate (C1) at (2.5,0);\n'
                '   \\coordinate (A) at (0,2); \\coordinate (B) at (1,2.5); \\coordinate (C) at (2.5,2);\n'
                '   \\draw (A1)--(C1) (A)--(B)--(C)--cycle (A)--(A1) (C)--(C1);\n'
                '   \\draw [dashed] (A1)--(B1)--(C1) (B)--(B1) (A)--(B1);\n'
                '   \\node [left] at (A) {$A$}; \\node [above] at (B) {$B$}; \\node [right] at (C) {$C$};\n'
                '   \\node [left] at (A1) {$A\'$}; \\node [below] at (B1) {$B\'$}; \\node [right] at (C1) {$C\'$};\n'
                '\\end{tikzpicture}\n'
                '\\end{center}'
            )


            # Nội dung lời giải
            loigiai = (
                'Ta có $AA\' \\perp (A\'B\'C\')$ nên $A\'B\'$ là hình chiếu vuông góc của $AB\'$ trên mặt phẳng $(A\'B\'C\')$. \\\\\n'
                'Do đó, $(AB\', (A\'B\'C\')) = (AB\', A\'B\') = \\widehat{AB\'A\'}$. \\\\\n'
                'Xét tam giác $AB\'A\'$ vuông tại $A\'$, ta có: \\\\\n'
                '$' + case['ly_luan'] + '. $ \\\\\n'
                'Suy ra $\\widehat{AB\'A\'} = ' + kq_str + '. $\\\\\n'
                'Vậy góc giữa đường thẳng $AB\'$ và mặt phẳng $(A\'B\'C\')$ bằng $' + kq_str + '$.'
            )
            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(kq_str).replace('^\\circ', '')

            # Xuất Content theo đúng định dạng ex-choice-loigiai
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' 
                + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{\n'
                + str(tikz_code) + '\n'
                + str(loigiai) + '\n'
                '}\n'
                '\\end{ex}\n'
                '\\end{minipage} \n\n')
            return content

