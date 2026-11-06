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


def bt_dang71_p4_b1_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Tìm cách random bài toán (Random tên các đỉnh)
                vertices = ['A', 'B', 'C', 'D']
                random.shuffle(vertices)
                V1, V2, V3, V4 = vertices  # V1 là đỉnh, V2, V3, V4 là đáy
                # M là trung điểm của V2V3 (tương ứng cạnh BC trong hình mẫu)

                # Đáp án đúng cho tứ diện đều là sqrt(3)/6
                kq_str = "\\frac{\\sqrt{3}}{6}"

                # Bước 4: Điều chỉnh các phương án sai không trùng đáp án đúng
                s = [
                    "\\frac{\\sqrt{2}}{2}",
                    "\\frac{\\sqrt{3}}{2}",
                    "\\frac{1}{2}",
                    "\\frac{\\sqrt{3}}{3}",
                    "\\frac{1}{3}",
                    "\\frac{\\sqrt{6}}{6}"
                ]
                random.shuffle(s)

                da_d = "\\True $" + kq_str + "$"
                das1 = "$" + s[0] + "$"
                das2 = "$" + s[1] + "$"
                das3 = "$" + s[2] + "$"

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                # Hình vẽ TikZ - Đã sửa cạnh BC (chứa BM) thành nét liền và thêm điểm đỏ
                tikz = (
                    "\\begin{center}\n"
                    "\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round]\n"
                    "   \\coordinate (D) at (0,0);\n"
                    "   \\coordinate (C) at (1.2,-0.8);\n"
                    "   \\coordinate (B) at (2.5,0.4);\n"
                    "   \\coordinate (A) at (1.3,2.5);\n"
                    "   \\coordinate (M) at ($(B)!0.5!(C)$);\n"
                    "   \\draw (A)--(D)--(C)--(A) (A)--(B)--(C) (D)--(C) (A)--(M);\n"
                    "   \\draw[dashed] (D)--(B) (D)--(M) ;\n"
                    "   \\fill[red] (A)  node[above, black] {" + V1 + "};\n"
                    "   \\fill[red] (B)  node[right, black] {" + V2 + "};\n"
                    "   \\fill[red] (C)  node[below, black] {" + V3 + "};\n"
                    "   \\fill[red] (D)  node[left, black] {" + V4 + "};\n"
                    "   \\fill[red] (M)  node[right, black] {M};\n"
                    "\\end{tikzpicture}\n"
                    "\\end{center}"
                )

                # Câu hỏi
                noidungcauhoi = (
                    "Cho tứ diện đều $" + V1 + V2 + V3 + V4 + "$, $M$ là trung điểm của cạnh $" + V2 + V3 + "$. "
                    "Tính $\\cos(" + V1 + V2 + ", " + V4 + "M)$" 
                )

                # Nội dung lời giải chi tiết
                loigiai = (
                    "Giả sử tứ diện đều $" + V1 + V2 + V3 + V4 + "$ có cạnh bằng $a$ ta có: "
                    "$ " + V4 + "M = \\frac{a\\sqrt{3}}{2} $. \\\\\n"
                    "Ta lại có: $\\cos(" + V1 + V2 + ", " + V4 + "M) = \\frac{|\\vec{" + V1 + V2 + "} \\cdot \\vec{" + V4 + "M}|}{|\\vec{" + V1 + V2 + "}| \\cdot |\\vec{" + V4 + "M}|}$. \\\\\n"
                    "Xét tích vô hướng: $\\vec{" + V1 + V2 + "} \\cdot \\vec{" + V4 + "M} = \\vec{" + V1 + V2 + "} \\cdot (\\vec{" + V4 + V2 + "} + \\vec{" + V2 + "M}) "
                    "= \\vec{" + V1 + V2 + "} \\cdot \\vec{" + V4 + V2 + "} + \\vec{" + V1 + V2 + "} \\cdot \\vec{" + V2 + "M}$. \\\\\n"
                    "Vì tứ diện đều nên các góc của các tam giác mặt bên đều bằng $60^\\circ$. \\\\\n"
                    "$\\vec{" + V1 + V2 + "} \\cdot \\vec{" + V4 + "M} = a \\cdot a \\cdot \\cos 60^\\circ + a \\cdot \\frac{a}{2} \\cdot \\cos 120^\\circ$ \\\\\n"
                    "$= \\frac{a^2}{2} - \\frac{a^2}{4} = \\frac{a^2}{4}$. \\\\\n"
                    "Thay vào công thức: $\\cos(" + V1 + V2 + ", " + V4 + "M) = \\frac{\\frac{a^2}{4}}{a \\cdot \\frac{a\\sqrt{3}}{2}} = \\frac{1}{2\\sqrt{3}} = \\frac{\\sqrt{3}}{6}$. \\\\\n"
                    "Vậy $\\cos(" + V1 + V2 + ", " + V4 + "M) = " + kq_str + "$."
                )

            # Xuất câu trắc nghiệm
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + tikz + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

