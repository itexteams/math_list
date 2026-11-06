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


def bt_dang22_p1_b2_c2_hh11(self):
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Khai báo các thành phần của câu hỏi
                noidung_hinhve = (
                    "\\begin{center}\n"
                    "\\begin{tikzpicture}[scale=0.8, line join=round, line cap=round, line width=1pt]\n"
                    "\\coordinate (A) at (0,0);\n"
                    "\\coordinate (B) at (-1.5,-1.2);\n"
                    "\\coordinate (C) at (2,-1.2);\n"
                    "\\coordinate (D) at (3.5,0);\n"
                    "\\coordinate (S) at (0,3);\n"
                    "\\coordinate (O) at (1, -0.6);\n"
                    "\\draw [dashed, line width=1pt] (S)--(A) (A)--(B) (A)--(D) (A)--(C) (B)--(D);\n"
                    "\\draw [line width=1pt] (S)--(B) (S)--(C) (S)--(D) (B)--(C) (C)--(D);\n"
                    "\\node at (A) [left] {$A$};\n"
                    "\\node at (B) [left] {$B$};\n"
                    "\\node at (C) [below] {$C$};\n"
                    "\\node at (D) [right] {$D$};\n"
                    "\\node at (S) [above] {$S$};\n"
                    "\\node at (O) [above] {$O$};\n"
                    "% Ký hiệu vuông góc tại A\n"
                    "\\draw (0,0.3)--(0.3,0.3)--(0.3,0);\n"
                    "\\end{tikzpicture}\n"
                    "\\end{center}"
                )

                noidungcauhoi = (
                    "Cho hình chóp $S.ABCD$ có đáy là hình vuông, cạnh bên $SA$ vuông góc với mặt đáy $(ABCD)$. Khẳng định nào sau đây \\textbf{sai}?\n"
                    + noidung_hinhve
                )

                # Bước 4: Định nghĩa các phương án (A là phương án sai - tức là đáp án đúng của câu hỏi)
                da_d = "\\True $CD \\perp (SBC)$"
                da_s1 = "$SA \\perp (ABC)$"
                da_s2 = "$BC \\perp (SAB)$"
                da_s3 = "$BD \\perp (SAC)$"

                # Trộn các phương án
                list_ans = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_ans)

                # Nội dung lời giải chi tiết
                loigiai = (
                    "Từ giả thiết, ta có: $SA \\perp (ABCD) \\Rightarrow SA \\perp (ABC)$. Do đó khẳng định $SA \\perp (ABC)$ là đúng.\\\\\n"
                    "Ta có: $\\left\\{\\begin{array}{l} BC \\perp AB \\text{ (do } ABCD \\text{ là hình vuông)} \\\\ BC \\perp SA \\text{ (do } SA \\perp (ABCD)\\text{)} \\end{array}\\right. \\Rightarrow BC \\perp (SAB)$. Do đó khẳng định $BC \\perp (SAB)$ là đúng.\\\\\n"
                    "Ta có: $\\left\\{\\begin{array}{l} BD \\perp AC \\text{ (tính chất đường chéo hình vuông)} \\\\ BD \\perp SA \\text{ (do } SA \\perp (ABCD)\\text{)} \\end{array}\\right. \\Rightarrow BD \\perp (SAC)$. Do đó khẳng định $BD \\perp (SAC)$ là đúng.\\\\\n"
                    "Vì các khẳng định trên đều đúng, nên khẳng định $CD \\perp (SBC)$ là khẳng định sai.\\\\ Chọn đáp án tương ứng với khẳng định $CD \\perp (SBC)$."
                )

            # Bước 2: Xuất nội dung theo mẫu (Không dùng raw string, xử lý ký tự đặc biệt)
            content = (
                "\\begin{minipage}{\\textwidth} \n"
                "\\begin{ex}\n" + str(noidungcauhoi) + "\n"
                "\\choice \n"
                "{" + str(list_ans[0]) + "}\n"
                "{" + str(list_ans[1]) + "}\n"
                "{" + str(list_ans[2]) + "}\n"
                "{" + str(list_ans[3]) + "}\n"
                "\\loigiai{" + str(loigiai) + "}\n"
                "\\end{ex}\n \\end{minipage} \n\n")
            return content

