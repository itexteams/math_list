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


def bt_dang44_p3_b3_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            a = symbols('a')

            # Danh sách các bộ dữ liệu ngẫu nhiên để đảm bảo kết quả là góc "đẹp" (30, 45, 60)
            # Mỗi bộ: (hệ số AB, góc BAC, hệ số SA, kết quả góc)
            data_options = [
                (2, 60, sqrt(2), 45),
                (2, 30, sqrt(3), 30),
                (1, 60, sqrt(2), 30),
                (4, 60, 2*sqrt(2), 45),
                (sqrt(2), 45, 1, 30)
            ]

            # Chọn ngẫu nhiên một bộ dữ liệu
            k_ab, deg_A, k_sa, target_angle = random.choice(data_options)

            # Thiết lập các giá trị toán học
            val_ab = k_ab * a
            val_sa = k_sa * a
            angle_A_rad = deg_A * pi / 180

            # Tính toán các đoạn thẳng phục vụ lời giải
            # HB = AB * sin(A)
            val_hb = val_ab * sin(angle_A_rad)
            # SB = sqrt(SA^2 + AB^2)
            val_sb = sqrt(val_sa**2 + val_ab**2)

            # Chuẩn bị chuỗi LaTeX cho các đại lượng
            ltx_ab = latex(val_ab)
            ltx_sa = latex(val_sa)
            ltx_hb = latex(val_hb)
            ltx_sb = latex(val_sb)
            ltx_sin = latex(val_hb / val_sb)

            # Tạo các phương án trắc nghiệm
            da_dung = '$' + str(target_angle) + '^\\circ$'
            options = [30, 45, 60, 90]
            if target_angle in options:
                options.remove(target_angle)
            random.shuffle(options)

            da_s1 = '$' + str(options[0]) + '^\\circ$'
            da_s2 = '$' + str(options[1]) + '^\\circ$'
            da_s3 = '$' + str(options[2]) + '^\\circ$'

            # Trộn đáp án
            list_ans = ['\\True ' + da_dung, da_s1, da_s2, da_s3]
            random.shuffle(list_ans)

            # Vẽ hình TikZ
            tikz_code = r"""\begin{center}
            \begin{tikzpicture}[scale=0.8, font=\small, line join=round, line cap=round, >=stealth, line width=1pt]
                \coordinate (A) at (0,0);
                \coordinate (B) at (1.5,-1.5);
                \coordinate (C) at (5,0);
                \coordinate (S) at (0,4);
                \coordinate (H) at (1.5,0); 
                \draw (S)--(A)--(B)--(S)--(C)--(B);
                \draw[dashed] (A)--(C) (S)--(H) (B)--(H);
                \tkzMarkRightAngle[size=0.2](S,A,C)
                \tkzMarkRightAngle[size=0.2](A,B,C)
                \tkzMarkRightAngle[size=0.2](B,H,C)
                \tkzLabelPoints[left](A,S)
                \tkzLabelPoints[right](C)
                \tkzLabelPoints[below](B)
                \tkzLabelPoints[above right](H)
                \node at (0.6,0.15) [rotate=0] {\tiny $""" + str(deg_A) + r"""^\circ$};
            \end{tikzpicture}
            \end{center}"""

            # Nội dung câu hỏi
            noidungcauhoi = ('Cho hình chóp $S.ABC$ có đáy là tam giác vuông tại $B$, cạnh bên $SA$ vuông góc với mặt đáy, '
                             '$AB = ' + ltx_ab + '$, $\\widehat{BAC} = ' + str(deg_A) + '^\\circ$ và $SA = ' + ltx_sa + '$. '
                             'Góc giữa đường thẳng $SB$ và mặt phẳng $\\left(SAC\\right)$ bằng bao nhiêu?')

            # Nội dung lời giải
            loigiai = ('Kẻ $BH \\perp AC \\left(H \\in AC\\right)$ và theo giả thiết $BH \\perp SA$ nên $BH \\perp \\left(SAC\\right)$. \\\\ '
                       'Do đó, $SH$ là hình chiếu vuông góc của $SB$ lên mặt phẳng $\\left(SAC\\right)$. \\\\ '
                       'Suy ra, $\\left(SB, \\left(SAC\\right)\\right) = \\left(SB, SH\\right) = \\widehat{BSH}$. \\\\ '
                       'Mà ta có: $SB = \\sqrt{SA^2 + AB^2} = ' + ltx_sb + '$, '
                       '$HB = AB \\cdot \\sin ' + str(deg_A) + '^\\circ = ' + ltx_hb + '$. \\\\ '
                       '$\\Rightarrow \\sin\\left(\\widehat{BSH}\\right) = \\frac{HB}{SB} = ' + ltx_sin + ' '
                       '\\Rightarrow \\widehat{BSH} = ' + str(target_angle) + '^\\circ$.')
            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(str(target_angle))
            # Xuất nội dung theo cấu trúc yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + noidungcauhoi + str(dapan)+
                       '\\loigiai{' + tikz_code+ loigiai + '}\n'
                       '\\end{ex}\n'
                       '\\end{minipage} \n\n')
            return content

