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


def bt_dang49_p4_b1_c2_hh11(self):
            # Khai báo biến
            # Danh sách các biến đại diện cho cạnh để random
            list_canh = ['a', 'x', 's', 'k']
            c = random.choice(list_canh)
            canh = symbols(c)

            # Tính toán các giá trị hình học (dùng sympy để giữ biểu thức căn)
            # Độ dài các đoạn thẳng trong tam giác MIC
            MI = canh / 2
            IC = (canh * sqrt(3)) / 2
            MC = (canh * sqrt(3)) / 2

            # Tính cosin góc MIC bằng định lý hàm số cos: cos(I) = (MI^2 + IC^2 - MC^2) / (2 * MI * IC)
            cos_val = (MI**2 + IC**2 - MC**2) / (2 * MI * IC)
            cos_final = sp.simplify(cos_val)

            # --- TẠO CÁC PHƯƠNG ÁN ---
            # Đáp án đúng
            da_dung = '$%s$' % latex(cos_final)

            # Danh sách các đáp án nhiễu (tránh trùng với đáp án đúng)
            ds_nhieu = [
                '$%s$' % latex(Rational(1, 2)),
                '$%s$' % latex(sqrt(3) / 4),
                '$%s$' % latex(sqrt(3) / 2),
                '$%s$' % latex(sqrt(2) / 2),
                '$%s$' % latex(Rational(1, 3)),
                '$%s$' % latex(sqrt(6) / 4)
            ]

            # Loại bỏ đáp án đúng khỏi danh sách nhiễu nếu lỡ trùng
            if da_dung in ds_nhieu:
                ds_nhieu.remove(da_dung)

            random.shuffle(ds_nhieu)
            das1 = ds_nhieu[0]
            das2 = ds_nhieu[1]
            das3 = ds_nhieu[2]

            # Trộn đáp án
            da_d = '\\True ' + da_dung
            list_ans = [da_d, das1, das2, das3]
            random.shuffle(list_ans)

            # --- TẠO HÌNH VẼ TIKZ ---
            # Tọa độ các điểm giả định để vẽ hình đẹp
            tikz_code = r"""\begin{center}
            \begin{tikzpicture}[scale=1, font=\footnotesize, line join=round, line cap=round]
                \coordinate (A) at (1.5,4);
                \coordinate (B) at (0,1.5);
                \coordinate (C) at (1.2,0);
                \coordinate (D) at (3.5,1.5);
                \coordinate (I) at ($(A)!0.5!(D)$);
                \coordinate (M) at ($(B)!0.5!(D)$);
                \draw (A)--(B)--(C)--cycle;
                \draw (A)--(C) (A)--(D)--(C) (I)--(C);
                \draw[dashed] (B)--(D) (I)--(M)--(C) ;
                \filldraw (A) circle (1pt) node[above] {$A$};
                \filldraw (B) circle (1pt) node[left] {$B$};
                \filldraw (C) circle (1pt) node[below] {$C$};
                \filldraw (D) circle (1pt) node[right] {$D$};
                \filldraw (I) circle (1pt) node[right] {$I$};
                \filldraw (M) circle (1pt) node[above] {$M$};
            \end{tikzpicture}
            \end{center}"""

            # --- NỘI DUNG CÂU HỎI ---
            noidungcauhoi = (
                'Cho tứ diện đều $ABCD$ cạnh $%s$. Tính cosin góc giữa hai đường thẳng $AB$ và $CI$, với $I$ là trung điểm của $AD$.'
                % latex(canh)
            )

            # --- LỜI GIẢI CHI TIẾT ---
            loigiai = (
                'Gọi $M$ là trung điểm của $BD$. \\\\'
                'Trong tam giác $ABD$, vì $I$ là trung điểm $AD$ và $M$ là trung điểm $BD$ nên $IM$ là đường trung bình, suy ra $IM // AB$. \\\\'
                'Khi đó, góc giữa hai đường thẳng $AB$ và $CI$ bằng góc giữa $IM$ và $CI$. \\\\'
                'Ta có: $(AB, CI) = (IM, IC)$. \\\\'
                'Suy ra: $\\cos(AB, IC) = \\cos(IM, IC) = |\\cos \\widehat{MIC}|$. \\\\'
                'Xét các cạnh của tam giác $MIC$: \\\\'
                '* $IM = \\frac{AB}{2} = \\frac{%s}{2}$. \\\\'
                '* $IC$ là đường cao trong tam giác đều $ACD$ cạnh $%s$ nên $IC = \\frac{%s\\sqrt{3}}{2}$. \\\\'
                '* $MC$ là đường cao trong tam giác đều $BCD$ cạnh $%s$ nên $MC = \\frac{%s\\sqrt{3}}{2}$. \\\\'
                'Áp dụng định lý hàm số cosin trong tam giác $MIC$, ta có: \\\\'
                '$\\cos \\widehat{MIC} = \\frac{MI^2 + IC^2 - MC^2}{2 \\cdot MI \\cdot IC} = '
                '\\frac{\\left(\\frac{%s}{2}\\right)^2 + \\left(\\frac{%s\\sqrt{3}}{2}\\right)^2 - \\left(\\frac{%s\\sqrt{3}}{2}\\right)^2}{2 \\cdot \\frac{%s}{2} \\cdot \\frac{%s\\sqrt{3}}{2}} = %s$. \\\\'
                'Vậy $\\cos(AB, IC) = |\\cos \\widehat{MIC}| = %s$.'
                % (latex(canh), latex(canh), latex(canh), latex(canh), latex(canh),
                   latex(canh), latex(canh), latex(canh), latex(canh), latex(canh),
                   latex(cos_final), latex(cos_final))
            )

            # --- XUẤT NỘI DUNG ---
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + noidungcauhoi + '\n'  
                '\\loigiai{' + tikz_code + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

