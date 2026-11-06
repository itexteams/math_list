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


def bt_dang46_p3_b3_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lis_edge = ['a', 'x', 's', 'b']
            edge_name = random.choice(lis_edge)

            # Tính toán các giá trị bằng Sympy
            tan_val = sqrt(2)/2
            tan_latex = latex(tan_val)

            # Tạo các phương án sai
            wrong_choices = [
                latex(sqrt(2)),
                latex(sqrt(3)),
                latex(sqrt(3)/3),
                latex(Rational(1, 2)),
                '1'
            ]
            random.shuffle(wrong_choices)
            das1, das2, das3 = wrong_choices[:3]

            # Nội dung câu hỏi
            noidungcauhoi = (
                'Cho tứ diện đều $ABCD$ có cạnh bằng $%s$. Gọi $M, N$ lần lượt là trung điểm của $BC$ và $AD$. '
                'Gọi $\\varphi$ là góc giữa đường thẳng $MN$ và mặt phẳng $\\left(BCD\\right)$. Giá trị $\\tan \\varphi$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).'
                % (edge_name)
            )

            # TikZ code vẽ hình chính xác theo mẫu
            tikz_code = (
                '\\begin{center}\n'
                '\\begin{tikzpicture}[scale=1.2, line join=round, line cap=round, >=stealth, line width=1pt]\n'
                '\\coordinate (A) at (2.5, 4.5);\n'
                '\\coordinate (B) at (0, 1);\n'
                '\\coordinate (D) at (4.5, 1);\n'
                '\\coordinate (C) at (2.2, -0.8);\n'
                '\\coordinate (M) at ($(B)!0.5!(C)$);\n'
                '\\coordinate (N) at ($(A)!0.5!(D)$);\n'
                '\\coordinate (H) at ($(M)!0.7!(D)$); \n'
                '\\draw (A)--(B)--(C)--(D)--(A) (A)--(C);\n'
                '\\draw (A)--(M);\n'
                '\\draw[dashed] (B)--(D) (M)--(D) (M)--(N) (N)--(H);\n'
                '\\begin{scope}[shift={(H)}, scale=0.25, dashed, line width=0.6pt]\n'
                '   \\coordinate (h1) at ($(M)-(H)$); \\coordinate (h2) at ($(N)-(H)$); \\coordinate (h3) at ($(D)-(H)$);\n'
                '   \\draw ($(h1)!1!(0,0)$)+($(h2)!1!(0,0)$ grap)--($(h1)!1!(0,0)$);\n' 
                '   \\draw ($(H)!0.25!(M)$)-|($(H)+(0,0.35)$);\n'
                '   \\draw ($(H)!0.25!(D)$)-|($(H)+(0,0.35)$);\n'
                '\\end{scope}\n'
                '\\draw[dashed, line width=0.7pt] ($(H)!0.25!(M)$)-|($(H)+(0,0.35)$);\n'
                '\\draw[dashed, line width=0.7pt] ($(H)!0.25!(D)$)-|($(H)+(0,0.35)$);\n'
                '\\foreach \\p/\\pos in {A/right, B/left, C/below, D/below right, M/below left, N/right, H/below}\n'
                '\\fill (\\p) circle (0pt) node[\\pos, black] {$\\p$};\n'
                '\\end{tikzpicture}\n'
                '\\end{center}'
            )
            h1=sqrt(2)/2
            number = Decimal(float(h1))  # Số cần làm tròn
            kq1 = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            kqz=str(kq1).replace('.', ',')
            # Lời giải chi tiết
            loigiai = (
                'Vì $ABCD$ là tứ diện đều cạnh $%s$ nên các mặt là các tam giác đều cạnh $%s$. \\\\'
                'Xét tam giác $BCD$ đều, $M$ là trung điểm $BC$ nên $DM \\perp BC$ và $DM = \\frac{%s\\sqrt{3}}{2}$. \\\\'
                'Xét tam giác $ABC$ đều, $M$ là trung điểm $BC$ nên $AM \\perp BC$ và $AM = \\frac{%s\\sqrt{3}}{2}$. \\\\'
                'Ta có $\\left(ABC\\right) \\cap \\left(BCD\\right) = BC$. Mà $AM \\perp BC$ và $DM \\perp BC$, suy ra $BC \\perp \\left(AMD\\right)$. \\\\'
                'Do $BC \\subset \\left(BCD\\right)$ nên $\\left(AMD\\right) \\perp \\left(BCD\\right)$ theo giao tuyến $MD$. \\\\'
                'Trong mặt phẳng $\\left(AMD\\right)$, kẻ $NH \\perp MD$ tại $H$. Khi đó $NH \\perp \\left(BCD\\right)$. \\\\'
                'Suy ra $HM$ là hình chiếu vuông góc của $NM$ lên mặt phẳng $\\left(BCD\\right)$. \\\\'
                'Do đó $\\varphi = \\left(MN, \\left(BCD\\right)\\right) = \\left(MN, MH\\right) = \\widehat{NMH} = \\widehat{NMD}$. \\\\'
                'Xét tam giác $AMD$ có $AM = MD = \\frac{%s\\sqrt{3}}{2}$ và $AD = %s$. \\\\'
                'Gọi $N$ là trung điểm $AD$, áp dụng công thức đường trung tuyến trong tam giác $AMD$: \\\\'
                '$MN^2 = \\frac{AM^2 + MD^2}{2} - \\frac{AD^2}{4} = \\frac{\\frac{3%s^2}{4} + \\frac{3%s^2}{4}}{2} - \\frac{%s^2}{4} = \\frac{%s^2}{2} \\implies MN = \\frac{%s\\sqrt{2}}{2}$. \\\\'
                'Trong tam giác $MND$, ta có $MN^2 + ND^2 = \\left(\\frac{%s\\sqrt{2}}{2}\\right)^2 + \\left(\\frac{%s}{2}\\right)^2 = \\frac{%s^2}{2} + \\frac{%s^2}{4} = \\frac{3%s^2}{4} = MD^2$. \\\\'
                'Suy ra tam giác $MND$ vuông tại $N$. \\\\'
                'Khi đó $\\tan \\varphi = \\tan \\widehat{NMD} = \\frac{ND}{MN} = \\frac{\\frac{%s}{2}}{\\frac{%s\\sqrt{2}}{2}} = \\frac{1}{\\sqrt{2}} = \\frac{\\sqrt{2}}{2} \\approx %s$.'
                % (edge_name, edge_name, edge_name, edge_name, edge_name, edge_name, edge_name, edge_name, edge_name, edge_name, edge_name, edge_name, edge_name, edge_name, edge_name, edge_name, edge_name, edge_name, kqz)
            )
            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(latex(kqz))
            # Các đáp án
            da_d = ('\\True $%s$' % tan_latex)
            da_s1 = ('$%s$' % das1)
            da_s2 = ('$%s$' % das2)
            da_s3 = ('$%s$' % das3)

            list_ans = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_ans)

            # Xuất nội dung
            content = (
                '\\begin{minipage}{\\textwidth}\n'
                '\\begin{ex}\n'
                + str(noidungcauhoi) +str(dapan)+
                '\\loigiai{' + str(tikz_code) + str(loigiai) + '}\n'
                '\\end{ex}\n'
                '\\end{minipage}\n\n')
            return content

