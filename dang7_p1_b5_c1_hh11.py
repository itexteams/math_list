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


def bt_dang7_p1_b5_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Hình vẽ TikZ theo đúng phong cách yêu cầu: nét vẽ 1pt, điểm 1pt, màu đen, không random điểm
        hinh_ve = (
            "\\begin{center}\n"
            "\\begin{tikzpicture}[scale=0.9, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "    \\coordinate (B1) at (0,0);\n"
            "    \\coordinate (C1) at (3,0);\n"
            "    \\coordinate (H1) at (1.5,0);\n"
            "    \\coordinate (A1) at (0.7,2.3);\n"
            "    \\draw[line width=1pt, black] (A1)--(B1)--(C1)--cycle;\n"
            "    \\draw[line width=1pt, black] (A1)--(H1);\n"
            "    \\fill[black] (A1) circle (1pt) node[above] {$A$};\n"
            "    \\fill[black] (B1) circle (1pt) node[below left] {$B$};\n"
            "    \\fill[black] (C1) circle (1pt) node[below right] {$C$};\n"
            "    \\fill[black] (H1) circle (1pt) node[below] {$H$};\n"
            "    \\node[below=0.6cm] at (H1) {Hình A};\n"
            "    \\coordinate (B2) at (4.5,0);\n"
            "    \\coordinate (C2) at (8.5,0);\n"
            "    \\coordinate (A2) at (5.7,2.3);\n"
            "    \\coordinate (D2) at (9.7,2.3);\n"
            "    \\coordinate (O2) at (intersection of A2--C2 and B2--D2);\n"
            "    \\draw[line width=1pt, black] (B2)--(C2)--(D2)--(A2)--cycle;\n"
            "    \\draw[line width=1pt, black] (A2)--(C2) (B2)--(D2);\n"
            "    \\fill[black] (A2) circle (1pt) node[above] {$A$};\n"
            "    \\fill[black] (B2) circle (1pt) node[below left] {$B$};\n"
            "    \\fill[black] (C2) circle (1pt) node[below right] {$C$};\n"
            "    \\fill[black] (D2) circle (1pt) node[above right] {$D$};\n"
            "    \\fill[black] (O2) circle (1pt) node[below] {$O$};\n"
            "    \\node[below=0.6cm] at ($(B2)!0.5!(C2)$) {Hình B};\n"
            "\\end{tikzpicture}\n"
            "\\end{center}"
        )

        # Nội dung câu hỏi (chuyển đổi || thành // theo quy tắc LaTeX)
        cauhoi_text = (
            "Cho hai hình vẽ sau:\\\\"
            "Trên Hình A có $\\begin{cases} AH \\perp BC \\\\ HB = HC \\end{cases}$ và trên Hình B có $\\begin{cases} AB // CD, AD // BC \\\\ AC \\perp BD \\end{cases}$\\\\"
            + hinh_ve + "Khẳng định nào sau đây là đúng?"
        )
        noidungcauhoi = "%s" % (cauhoi_text)

        # Các mệnh đề đơn lẻ
        menh_de_1 = "$\\triangle ABC$ là tam giác cân tại $A$"
        menh_de_2 = "Tứ giác $ABCD$ là hình thoi"

        # Đáp án đúng
        du = [
            "Cả hai khẳng định (\"%s\" và \"%s\") đều đúng" % (menh_de_1, menh_de_2)
        ]
        da = random.choice(du)

        # Các đáp án sai
        s = [
            "Chỉ có khẳng định \"%s\" là đúng" % (menh_de_1),
            "Chỉ có khẳng định \"%s\" là đúng" % (menh_de_2),
            "$\\triangle ABC$ là tam giác đều",
            "Tứ giác $ABCD$ là hình chữ nhật",
            "Cả hai khẳng định (\"%s\" và \"%s\") đều sai" % (menh_de_1, menh_de_2)
        ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Các phương án
        da_d = "\\True " + str(da)
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào danh sách ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Lời giải chi tiết, khoa học, không viết tắt, xuống dòng bằng \\\\, dùng // thay cho ||
        loigiai_text = (
            "Xét từng hình vẽ:\\\\"
            "+ Đối với Hình A:\\\\"
            "Tam giác $ABC$ có đoạn thẳng $AH \\perp BC$ tại $H$ nên $AH$ là đường cao của tam giác $ABC$.\\\\"
            "Mặt khác, $HB = HC$ nên $H$ là trung điểm của $BC$, suy ra $AH$ đồng thời là đường trung tuyến của tam giác $ABC$.\\\\"
            "Tam giác có đường cao vừa là đường trung tuyến xuất phát từ cùng một đỉnh thì tam giác đó là tam giác cân.\\\\"
            "Do đó, tam giác $ABC$ cân tại $A$.\\\\"
            "+ Đối với Hình B:\\\\"
            "Tứ giác $ABCD$ có các cặp cạnh đối song song: $AB // CD$ và $AD // BC$ nên $ABCD$ là hình bình hành.\\\\"
            "Mặt khác, hai đường chéo của tứ giác vuông góc với nhau tại $O$ ($AC \\perp BD$).\\\\"
            "Hình bình hành có hai đường chéo vuông góc với nhau là hình thoi.\\\\"
            "Do đó, tứ giác $ABCD$ là hình thoi.\\\\"
            "Vậy cả hai khẳng định trên đều đúng."
        )
        loigiai = "%s" % (loigiai_text)

    # Xuất câu trắc nghiệm
    content = (
        '\\begin{minipage}{\\textwidth}\n'
        '\\begin{ex}\n' +
        str(noidungcauhoi) + '\n'
        '\\choice\n'
        '{' + str(list_1[0]) + '}\n'
        '{' + str(list_1[1]) + '}\n'
        '{' + str(list_1[2]) + '}\n'
        '{' + str(list_1[3]) + '}\n'
        '\\loigiai{' + str(loigiai) + '}\n'
        '\\end{ex}\n'
        '\\end{minipage}\n\n')
    return content

