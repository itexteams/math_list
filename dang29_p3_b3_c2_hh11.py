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


def bt_dang29_p3_b3_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu cho LaTeX
            a = symbols('a')

            # Bước 1 & 3: Nghiên cứu đề bài và thiết lập các bộ số ngẫu nhiên để bài toán luôn có kết quả đẹp
            # Cấu hình: AB, AD, SA (tất cả nhân với a)
            # Loại 1: AB=k, AD=k*sqrt(3), SA=k*sqrt(2) => Góc 30 độ (Giống ảnh)
            # Loại 2: AB=k, AD=k, SA=k => Góc 30 độ
            # Loại 3: AB=k*sqrt(3), AD=k, SA=k*sqrt(2) => Góc 30 độ
            configs = [
                {'ab': 1, 'ad': sqrt(3), 'sa': sqrt(2), 'ans': 30},
                {'ab': 1, 'ad': 1, 'sa': 1, 'ans': 30},
                {'ab': sqrt(3), 'ad': 1, 'sa': sqrt(2), 'ans': 30}
            ]

            config = random.choice(configs)
            k = random.randint(1, 4) # Hệ số nhân thêm để bài toán đa dạng

            # Tính toán các giá trị cụ thể
            val_ab = k * config['ab']
            val_ad = k * config['ad']
            val_sa = k * config['sa']
            val_bc = val_ad
            ans_val = config['ans']

            # Biểu thức LaTeX cho các cạnh
            tex_ab = latex(val_ab * a).replace('1.0', '')
            tex_ad = latex(val_ad * a).replace('1.0', '')
            tex_sa = latex(val_sa * a).replace('1.0', '')
            tex_bc = tex_ad

            # Tính toán BH và SB cho lời giải
            # BH = (AB*BC) / sqrt(AB^2 + BC^2)
            bh_num = val_ab * val_bc
            bh_den = sqrt(val_ab**2 + val_bc**2)
            val_bh = bh_num / bh_den
            tex_bh = latex(val_bh * a)

            # SB = sqrt(SA^2 + AB^2)
            val_sb = sqrt(val_sa**2 + val_ab**2)
            tex_sb = latex(val_sb * a)

            # sin(BSH) = BH / SB
            val_sin = val_bh / val_sb
            tex_sin = latex(val_sin)

            # Bước 4: Điều chỉnh các phương án sai
            wrong_ans = {15, 45, 60, 75, 90}
            if ans_val in wrong_ans:
                wrong_ans.remove(ans_val)
            list_wrong = random.sample(list(wrong_ans), 3)

            da_d = "\\True $" + str(ans_val) + "^\\circ$"
            da_s1 = '$'+str(list_wrong[0]) + "^\\circ$"
            da_s2 = '$'+str(list_wrong[1]) + "^\\circ$"
            da_s3 = '$'+str(list_wrong[2]) + "^\\circ$"

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Hình vẽ TikZ
            tikz_code = r"""\begin{center}
            \begin{tikzpicture}[scale=1, line join=round, line cap=round, line width=1pt]
                \coordinate (A) at (0,0);
                \coordinate (B) at (-1.5,-1.5);
                \coordinate (D) at (4,0);
                \coordinate (C) at ($(B)+(D)-(A)$);
                \coordinate (S) at (0,3.5);
                \coordinate (H) at ($(A)!0.35!(C)$);
                \draw (S)--(B)--(C)--(D)--(S)--(C);
                \draw[dashed] (S)--(A)--(B) (A)--(D) (A)--(C) (S)--(H) (B)--(H);
                \draw (A) node[left]{$A$} (B) node[below left]{$B$} (C) node[below right]{$C$} 
                      (D) node[right]{$D$} (S) node[above]{$S$} (H) node[below right]{$H$};
                \tkzMarkRightAngle(S,A,B)
                \tkzMarkRightAngle(S,A,D)
                \tkzMarkRightAngle(B,H,A)
            \end{tikzpicture}
            \end{center}"""

            # Bước 2: Viết lại nội dung bài toán
            noidungcauhoi = (
                "Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình chữ nhật, cạnh $AB = %s$, $AD = %s$. "
                "Cạnh bên $SA = %s$ và vuông góc với mặt phẳng đáy. Góc giữa đường thẳng $SB$ và mặt phẳng $(SAC)$ bằng bao nhiêu?"
                % (tex_ab, tex_ad, tex_sa)
            )

            loigiai = (
                "Kẻ $BH \\perp AC$ tại $H \\in AC$. \\\\"
                "Vì $SA \\perp (ABCD)$ nên $SA \\perp BH$. \\\\"
                "Ta có $\\left\\{ \\begin{array}{l} BH \\perp AC \\\\ BH \\perp SA \\end{array} \\right. \\implies BH \\perp (SAC)$. \\\\"
                "Khi đó $SH$ là hình chiếu vuông góc của $SB$ trên mặt phẳng $(SAC)$. \\\\"
                "Do đó góc giữa đường thẳng $SB$ và mặt phẳng $(SAC)$ là góc $\\widehat{BSH}$. \\\\"
                "Trong tam giác vuông $ABC$, ta có đường cao $BH$: \\\\"
                "$BH = \\frac{AB \\cdot BC}{\\sqrt{AB^2 + BC^2}} = \\frac{%s \\cdot %s}{\\sqrt{\\left(%s\\right)^2 + \\left(%s\\right)^2}} = %s$. \\\\"
                "Trong tam giác vuông $SAB$, ta có: \\\\"
                "$SB = \\sqrt{SA^2 + AB^2} = \\sqrt{\\left(%s\\right)^2 + \\left(%s\\right)^2} = %s$. \\\\"
                "Trong tam giác vuông $SBH$ (vuông tại $H$ vì $BH \\perp (SAC) \\implies BH \\perp SH$), ta có: \\\\"
                "$\\sin \\widehat{BSH} = \\frac{BH}{SB} = \\frac{%s}{%s} = %s$. \\\\"
                "Vậy $\\widehat{BSH} = %s^\\circ$."
                % (tex_ab, tex_bc, tex_ab, tex_bc, tex_bh, tex_sa, tex_ab, tex_sb, tex_bh, tex_sb, tex_sin, ans_val)
            )
            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(latex(ans_val))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + tikz_code+ str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

