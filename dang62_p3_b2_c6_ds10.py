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


def bt_dang62_p3_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang = [1, 2, 3, 4]
            dang = random.choice(lisdang)

            # Thiết lập các thông số dựa trên dạng bài được random
            if dang == 1:
                target_text = "nằm trên các đường chéo của hình vuông"
                nA = 70
                nA_explanation = 'Gọi biến cố $A$: "Ba bóng đèn đó nằm trên các đường chéo của hình vuông".\\\\\nVậy số cách chọn $A$ thuận lợi: $n(A) = 2.C_7^3 = 70$ cách.'
            elif dang == 2:
                target_text = "nằm trên các cạnh của hình vuông"
                nA = 4
                nA_explanation = 'Gọi biến cố $A$: "Ba bóng đèn đó nằm trên các cạnh của hình vuông".\\\\\nVậy số cách chọn $A$ thuận lợi: $n(A) = 4.C_3^3 = 4$ cách.'
            elif dang == 3:
                target_text = "nằm trên các đường thẳng nối trung điểm hai cạnh đối diện của hình vuông"
                nA = 2
                nA_explanation = 'Gọi biến cố $A$: "Ba bóng đèn đó nằm trên các đường thẳng nối trung điểm hai cạnh đối diện của hình vuông".\\\\\nVậy số cách chọn $A$ thuận lợi: $n(A) = 2.C_3^3 = 2$ cách.'
            elif dang == 4:
                target_text = "không nằm trên các đường chéo của hình vuông"
                nA = 14
                nA_explanation = 'Gọi biến cố $A$: "Ba bóng đèn đó không nằm trên các đường chéo của hình vuông".\\\\\nVậy số cách chọn $A$ thuận lợi: $n(A) = 84 - 70 = 14$ cách.'

            # Tính toán xác suất đúng
            n_Omega = 84
            prob = nA / n_Omega
            ans_val = round(prob, 2)
            ans_str = f"{ans_val:.2f}".replace('.', ',')

            # Tạo các đáp án sai nhiễu
            distractors = [
                round(nA / 74, 2),
                round(nA / 76, 2),
                round((nA + 2) / 84, 2),
                round(abs(nA - 2) / 84, 2) if nA - 2 > 0 else round((nA + 4) / 84, 2),
                round(nA / 17, 2),
                round(nA / math.comb(17, 3), 2)
            ]

            wrong_vals = set()
            for d in distractors:
                if d != ans_val and 0 < d < 1:
                    wrong_vals.add(f"{d:.2f}".replace('.', ','))

            # Nếu chưa đủ 3 đáp án nhiễu, random thêm
            while len(wrong_vals) < 3:
                w = round(random.uniform(0.01, 0.99), 2)
                if w != ans_val:
                    wrong_vals.add(f"{w:.2f}".replace('.', ','))

            wrong_list = list(wrong_vals)[:3]

            # Các đáp án trắc nghiệm
            da_d = '\\True $%s$' % ans_str
            da_s1 = '$%s$' % wrong_list[0]
            da_s2 = '$%s$' % wrong_list[1]
            da_s3 = '$%s$' % wrong_list[2]

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Hình vẽ TikZ
            tikz_code = (
                '\\begin{tikzpicture}[scale=0.8, line width=1pt]\n'
                '\\draw (-3,-3) rectangle (3,3);\n'
                '\\draw (-3,3) -- (3,-3);\n'
                '\\draw (-3,-3) -- (3,3);\n'
                '\\fill[orange] (0,0) circle (3pt);\n'
                '\\fill[blue] (-3,3) circle (3pt);\n'
                '\\fill[orange] (3,3) circle (3pt);\n'
                '\\fill[magenta] (-3,-3) circle (3pt);\n'
                '\\fill[green] (3,-3) circle (3pt);\n'
                '\\fill[red] (0,3) circle (3pt);\n'
                '\\fill[red] (0,-3) circle (3pt);\n'
                '\\fill[red] (-3,0) circle (3pt);\n'
                '\\fill[pink] (3,0) circle (3pt);\n'
                '\\fill[red] (-2,2) circle (3pt);\n'
                '\\fill[green] (-1,1) circle (3pt);\n'
                '\\fill[red] (1,-1) circle (3pt);\n'
                '\\fill[magenta] (2,-2) circle (3pt);\n'
                '\\fill[green] (-2,-2) circle (3pt);\n'
                '\\fill[purple] (-1,-1) circle (3pt);\n'
                '\\fill[green] (1,1) circle (3pt);\n'
                '\\fill[magenta] (2,2) circle (3pt);\n'
                '\\end{tikzpicture}\n'
            )

            # Câu hỏi
            noidungcauhoi = (
                '\\immini{Trên một biển quảng cáo hình vuông, người ta gắn $17$ bóng đèn tại các vị trí đặc biệt bao gồm: '
                '$4$ đỉnh, tâm hình vuông và các điểm chia đều các cạnh cũng như các đường chéo. '
                'Cấu trúc phân bố điểm đảm bảo rằng trên mỗi đường chéo có đúng $7$ bóng đèn và trên mỗi cạnh hình vuông có đúng $3$ bóng đèn. '
                'Tại một thời điểm, có ba bóng đèn bất kỳ vụt sáng. Biết rằng ba bóng đèn này không tạo thành một tam giác. '
                'Tính xác suất để ba bóng đèn đó %s (Kết quả làm tròn đến hàng phần trăm).}{%s}' % (target_text, tikz_code)
            )

            # Nội dung lời giải
            loigiai = (
                'Số phần tử không gian mẫu: Trên $2$ đường chéo, mỗi đường chéo có $7$ điểm.\\\\\n'
                'Số cách chọn $3$ điểm thẳng hàng là: $2.C_7^3 = 70$ cách.\\\\\n'
                'Trên $4$ cạnh, mỗi cạnh có đúng $3$ điểm thẳng hàng nên số cách chọn là: $4.C_3^3 = 4$ (cách).\\\\\n'
                'Trên các đường trung trực, có $2$ đường nối trung điểm các cạnh đối diện đi qua tâm, mỗi đường có $3$ điểm nên số cách chọn là: $2.C_3^3 = 2$ (cách).\\\\\n'
                'Trên các đường thẳng nối từ trung điểm cạnh, đi qua một điểm trên đường chéo tới đỉnh đối diện có $8$ đường thẳng, mỗi đường chứa đúng $3$ điểm nên có $8.C_3^3 = 8$ cách chọn.\\\\\n'
                'Vậy số phần tử trong không gian mẫu: $n(\\Omega) = 70 + 4 + 2 + 8 = 84$ (cách).\\\\\n'
                'Số cách chọn thuận lợi:\\\\\n'
                '%s\\\\\n'
                'Xác suất cần tìm là $P(A) = \\frac{n(A)}{n(\\Omega)} = \\frac{%s}{84} \\approx %s$.' % (nA_explanation, nA, ans_str)
            )
            dapan='\\shortans[0]{$%s$}\n'%(ans_str)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                       '\\loigiai{\n' + str(loigiai) + '\n}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content

