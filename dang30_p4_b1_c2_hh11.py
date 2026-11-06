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


def bt_dang30_p4_b1_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Biến số học (trong bài này góc là cố định 60 độ, ta random tên cạnh hoặc ký hiệu)
                canh = random.choice(['a', 'x', 'm', '1'])

                # Đáp án đúng
                kq = '60^\\circ'
                da_d = '\\True $%s$' % (kq)

                # Các đáp án nhiễu
                s = ['$30^\\circ$', '$45^\\circ$', '$90^\\circ$']
                random.shuffle(s)
                da_s1 = s[0]
                da_s2 = s[1]
                da_s3 = s[2]

                # Trộn thứ tự đáp án cho phần choice
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Hình vẽ TikZ cho hình lập phương
                # Lưu ý: Trong Python string không dùng r'', ta phải dùng \\ để biểu thị dấu gạch chéo ngược
                tikz_image = (
                    '\\begin{center}\n'
                    '\\begin{tikzpicture}[scale=1.5, line join=round, line cap=round]\n'
                    '  \\coordinate (A\') at (0,0);\n'
                    '  \\coordinate (B\') at (2,0);\n'
                    '  \\coordinate (D\') at (0.8,0.6);\n'
                    '  \\coordinate (C\') at (2.8,0.6);\n'
                    '  \\coordinate (A) at (0,2);\n'
                    '  \\coordinate (B) at (2,2);\n'
                    '  \\coordinate (D) at (0.8,2.6);\n'
                    '  \\coordinate (C) at (2.8,2.6);\n'
                    '  \\draw (A) -- (B) -- (C) -- (D) -- cycle;\n'
                    '  \\draw (A) -- (A\') -- (B\') -- (B);\n'
                    '  \\draw (B\') -- (C\') -- (C);\n'
                    '  \\draw[dashed] (A\') -- (D\') -- (C\');\n'
                    '  \\draw[dashed] (D) -- (D\');\n'
                    '  \\draw (A) -- (B\');\n'
                    '  \\draw[dashed] (A\') -- (C\');\n'
                    '  \\draw (A) -- (C) -- (B\');\n'
                    '  \\node[left] at (A) {$A$};\n'
                    '  \\node[right] at (B) {$B$};\n'
                    '  \\node[right] at (C) {$C$};\n'
                    '  \\node[left] at (D) {$D$};\n'
                    '  \\node[left] at (A\') {$A\'$};\n'
                    '  \\node[right] at (B\') {$B\'$};\n'
                    '  \\node[right] at (C\') {$C\'$};\n'
                    '  \\node[left] at (D\') {$D\'$};\n'
                    '\\end{tikzpicture}\n'
                    '\\end{center}'
                )

                # Nội dung câu hỏi
                noidungcauhoi = (
                    'Cho hình lập phương $ABCD.A\'B\'C\'D\'$. Tính góc giữa hai đường thẳng $AB\'$ và $A\'C\'$.'
                )

                # Nội dung lời giải chi tiết
                loigiai = (
                    'Giả sử hình lập phương $ABCD.A\'B\'C\'D\'$ có cạnh là $%s$. \\\\\n'
                    'Do $AC \\parallel A\'C\'$ nên góc giữa hai đường thẳng $AB\'$ và $A\'C\'$ bằng góc giữa hai đường thẳng $AB\'$ và $AC$. \\\\\n'
                    'Ta xét tam giác $AB\'C$, ta có: \\\\\n'
                    '$AB\' = AC = CB\' = %s\\sqrt{2}$ (vì đều là các đường chéo của các mặt hình vuông bằng nhau). \\\\\n'
                    '$\\Rightarrow$ Tam giác $AB\'C$ là tam giác đều, nên $\\widehat{CAB\'} = 60^\\circ$. \\\\\n'
                    'Vậy $(AB\', A\'C\') = (AB\', AC) = \\widehat{CAB\'} = 60^\\circ$.'
                    % (latex(canh), latex(canh) if canh != '1' else '')
                )

            # Xuất câu trắc nghiệm theo định dạng yêu cầu (không dùng tiền tố r)
            content = (
                '\\begin{minipage}{\\textwidth}\n'
                '\\begin{ex}\n'
                + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(tikz_image) + '\n'+ str(loigiai) + '}\n'
                '\\end{ex}\n'
                '\\end{minipage}\n\n')
            return content

