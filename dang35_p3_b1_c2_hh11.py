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


def bt_dang35_p3_b1_c2_hh11(self):
            # Khai báo biến
            # --- Bước 1: Khai báo biến và Random ---
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Giả sử cạnh hình lập phương là a (để tổng quát)
                # Trong bài này kết quả góc giữa AM và BC' luôn là 45 độ
                # Chúng ta sẽ random các bộ nhãn đỉnh nếu cần, nhưng ở đây giữ nguyên theo đề bài 
                # và tập trung vào việc tạo ra các phương án nhiễu.

                ans_correct = '45^\\circ'
                distractors = ['30^\\circ', '60^\\circ', '90^\\circ', '120^\\circ']

                random.shuffle(distractors)
                da_d = '\\True $' + ans_correct + '$'
                da_s1 = '$' + distractors[0] + '$'
                da_s2 = '$' + distractors[1] + '$'
                da_s3 = '$' + distractors[2] + '$'

                # Trộn thứ tự đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # --- Bước 2: Viết nội dung câu hỏi ---
                noidungcauhoi = (
                    'Cho hình lập phương $ABCD.A\'B\'C\'D\'$; gọi $M$ là trung điểm của $B\'C\'$. '
                    'Góc giữa hai đường thẳng $AM$ và $BC\'$ bằng bao nhiêu? (làm tròn kết quả đến hàng đơn vị).'
                )

                # --- Bước 3: Vẽ hình bằng TikZ ---
                # Hình vẽ mô phỏng lại phối cảnh của hình lập phương trong ảnh
                tikz_code = (
                    '\\begin{center}\n'
                    '\\begin{tikzpicture}[scale=2, line join=round, line cap=round, >=stealth]\n'
                    '  \\coordinate (A\') at (0,0);\n'
                    '  \\coordinate (D\') at (2,0);\n'
                    '  \\coordinate (B\') at (0.8,0.6);\n'
                    '  \\coordinate (C\') at (2.8,0.6);\n'
                    '  \\coordinate (A) at (0,2);\n'
                    '  \\coordinate (D) at (2,2);\n'
                    '  \\coordinate (B) at (0.8,2.6);\n'
                    '  \\coordinate (C) at (2.8,2.6);\n'
                    '  \\coordinate (M) at ($(B\')!0.5!(C\')$);\n'
                    '  \\coordinate (N) at ($(B)!0.5!(B\')$);\n'
                    '  \n'
                    '  \\draw (A) -- (D) -- (D\') -- (A\') -- cycle;\n'
                    '  \\draw (A) -- (B) -- (C) -- (D);\n'
                    '  \\draw (C) -- (C\') -- (D\');\n'
                    '  \\draw[dashed] (A\') -- (B\') -- (C\');\n'
                    '  \\draw[dashed] (B) -- (B\') -- (M);\n'
                    '  \\draw[dashed] (A) -- (M) -- (N) -- (A);\n'
                    '  \\draw[dashed] (B) -- (C\') -- (M);\n'
                    '  \\draw[dashed] (A\') -- (M);\n'
                    '  \n'
                    '  \\fill (M) circle (0.5pt) node[below] {$M$};\n'
                    '  \\fill (N) circle (0.5pt) node[left] {$N$};\n'
                    '  \\node[left] at (A) {$A$};\n'
                    '  \\node[above] at (B) {$B$};\n'
                    '  \\node[right] at (C) {$C$};\n'
                    '  \\node[right] at (D) {$D$};\n'
                    '  \\node[left] at (A\') {$A\'$};\n'
                    '  \\node[below left] at (B\') {$B\'$};\n'
                    '  \\node[right] at (C\') {$C\'$};\n'
                    '  \\node[right] at (D\') {$D\'$};\n'
                    '\\end{tikzpicture}\n'
                    '\\end{center}'
                )

                # --- Bước 4: Soạn thảo lời giải chi tiết ---
                # Sử dụng latex() cho các biểu thức toán học
                a = symbols('a')
                a_m_sq = Rational(9, 4) * a**2
                a_n_sq = Rational(5, 4) * a**2
                mn_sq = Rational(2, 4) * a**2

                loigiai = (
                    'Giả sử cạnh của hình lập phương là $a > 0$. \\\\\n'
                    'Gọi $N$ là trung điểm đoạn thẳng $BB\'$. Khi đó, $MN // BC\'$ nên '
                    '$(AM, BC\') = (AM, MN)$. \\\\\n'
                    'Xét tam giác $A\'B\'M$ vuông tại $B\'$ ta có: '
                    '$A\'M = \\sqrt{A\'B\'^2 + B\'M^2} = \\sqrt{a^2 + \\frac{a^2}{4}} = \\frac{a\\sqrt{5}}{2}$. \\\\\n'
                    'Xét tam giác $AA\'M$ vuông tại $A\'$ ta có: '
                    '$AM = \\sqrt{AA\'^2 + A\'M^2} = \\sqrt{a^2 + \\frac{5a^2}{4}} = \\frac{3a}{2}$. \\\\\n'
                    'Có $AN = A\'M = \\frac{a\\sqrt{5}}{2}$; $MN = \\frac{BC\'}{2} = \\frac{a\\sqrt{2}}{2}$. \\\\\n'
                    'Trong tam giác $AMN$ ta có: \\\\\n'
                    '$\\cos \\widehat{AMN} = \\frac{MA^2 + MN^2 - AN^2}{2 \\cdot MA \\cdot MN} = '
                    '\\frac{\\frac{9a^2}{4} + \\frac{2a^2}{4} - \\frac{5a^2}{4}}{2 \\cdot \\frac{3a}{2} \\cdot \\frac{a\\sqrt{2}}{2}} = '
                    '\\frac{\\frac{6a^2}{4}}{\\frac{3a^2\\sqrt{2}}{2}} = \\frac{1}{\\sqrt{2}}$. \\\\\n'
                    'Suy ra $\\widehat{AMN} = 45^\\circ$.'
                )
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(45))

            # --- Bước 5: Xuất nội dung ---
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + tikz_code + '\n'+ str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

