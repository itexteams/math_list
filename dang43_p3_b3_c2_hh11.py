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


def bt_dang43_p3_b3_c2_hh11(self):
            # Khai báo biến
            # Khai báo danh sách các dạng (ở đây là 1 dạng chính)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Suy nghĩ tìm cách random bài toán
                # Ta có thể random tên các đỉnh hoặc biến số cạnh. 
                # Ở đây ta chọn ngẫu nhiên tên biến cạnh là a, x, hoặc s.
                bien_canh = random.choice(['a', 'x', 's'])

                # Kết quả sin(alpha) luôn là 1/2 đối với hình lập phương trong trường hợp này
                kq_value = Rational(1, 2)
                da_dung = '$' + latex(kq_value) + '$'

                # B4: Điều chỉnh các phương án sai (không được trùng với 1/2)
                ds_sai = [
                    '$' + latex(sqrt(3)/4) + '$',
                    '$' + latex(sqrt(3)/2) + '$',
                    '$' + latex(sqrt(3)/5) + '$',
                    '$' + latex(Rational(1, 3)) + '$',
                    '$' + latex(sqrt(2)/2) + '$',
                    '$' + latex(Rational(2, 3)) + '$'
                ]

                random.shuffle(ds_sai)
                das1 = ds_sai[0]
                das2 = ds_sai[1]
                das3 = ds_sai[2]

                # Câu hỏi
                noidungcauhoi = ('Cho hình lập phương $ABCD.A\'B\'C\'D\'$ có cạnh bằng $' + bien_canh + '$, gọi $\\alpha$ là góc giữa đường thẳng $A\'B$ và mặt phẳng $\\left( BB\'D\'D \\right)$. Giá trị $\\sin \\alpha$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).')

                # Các đáp án
                da_d = '\\True ' + da_dung
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                # Hình vẽ TikZ
                hinh_ve = (
                    '\\begin{center}\n'
                    '\\begin{tikzpicture}[line join=round, line cap=round, font=\\footnotesize, scale=0.7, line width=1pt]\n'
                    '\\coordinate (A1) at (0,0); \\coordinate (B1) at (1.5,1.2); \\coordinate (D1) at (4,0);\n'
                    '\\coordinate (C1) at ($(B1)+(D1)-(A1)$); \\coordinate (A) at (0,4);\n'
                    '\\coordinate (B) at ($(A)+(B1)-(A1)$); \\coordinate (D) at ($(A)+(D1)-(A1)$);\n'
                    '\\coordinate (C) at ($(B)+(D)-(A)$); \\coordinate (H) at ($(A1)!0.5!(C1)$);\n'
                    '\\draw (A)--(B)--(C)--(D)--cycle; \\draw (A)--(A1) (D)--(D1) (C)--(C1);\n'
                    '\\draw (B)--(C) (C)--(D) (A1)--(D1) (C1)--(D1);\n'
                    '\\draw[dashed] (A1)--(B1)--(C1) (B1)--(B)  (B)--(D1) (B1)--(D1) (A1)--(C1) (B)--(H) (A1)--(B);\n'
                    '\\draw (A1) node[below left]{$A\'$}; \\draw (B1) node[above left]{$B\'$};\n'
                    '\\draw (C1) node[right]{$C\'$}; \\draw (D1) node[below right]{$D\'$};\n'
                    '\\draw (A) node[left]{$A$}; \\draw (B) node[above]{$B$};\n'
                    '\\draw (C) node[above right]{$C$}; \\draw (D) node[right]{$D$};\n'
                    '\\draw (H) node[below]{$H$};\n'
                    '\\end{tikzpicture}\n'
                    '\\end{center}'
                )

                loigiai = (
                    hinh_ve + '\n'
                    'Gọi $H$ là tâm hình vuông $A\'B\'C\'D\'$. \\\\\n'
                    'Ta có $A\'H \\perp B\'D\'$ (tính chất đường chéo hình vuông) và $A\'H \\perp BB\'$ (do $BB\'$ vuông góc với mặt đáy). \\\\\n'
                    'Suy ra $A\'H \\perp \\left( BB\'D\'D \\right)$. \\\\\n'
                    'Khi đó, $BH$ là hình chiếu vuông góc của $A\'B$ trên mặt phẳng $\\left( BB\'D\'D \\right)$. \\\\\n'
                    'Do đó $\\left( A\'B, \\left( BB\'D\'D \\right) \\right) = \\widehat{A\'BH} = \\alpha$. \\\\\n'
                    'Xét tam giác $A\'HB$ vuông tại $H$, ta có: \\\\\n'
                    '$\\sin \\alpha = \\frac{A\'H}{A\'B}$. \\\\\n'
                    'Với $A\'H = \\frac{1}{2} A\'C\' = \\frac{' + bien_canh + '\\sqrt{2}}{2}$ và $A\'B = ' + bien_canh + '\\sqrt{2}$ (đường chéo của mặt bên). \\\\\n'
                    'Vậy $\\sin \\alpha = \\frac{\\frac{' + bien_canh + '\\sqrt{2}}{2}}{' + bien_canh + '\\sqrt{2}} = \\frac{1}{2} = 0,5$.'
                )
                #Đáp án
                dapan='\\shortans[0]{$0,5$}\n'
            # Xuất câu trắc nghiệm
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

