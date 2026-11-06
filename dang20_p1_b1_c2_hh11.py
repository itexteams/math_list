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


def bt_dang20_p1_b1_c2_hh11(self):
            # Khai báo biến
            # Ta sẽ random giữa 2 cấu hình hình học để ra các góc khác nhau
            kich_ban = random.choice(['120_deg', '90_deg'])

            ky_hieu = random.choice(['a', 'b', 'x', 'y', 'm'])
            val_a = symbols(ky_hieu)

            if kich_ban == '120_deg':
                # Giả thiết: BC = a*sqrt(2), các cạnh khác = a
                val_BC = '%s\\sqrt{2}' % (latex(val_a))
                goc_kq = 120
                text_tam_giac_abc = 'vuông tại $A$ (do $AB^2 + AC^2 = BC^2$)'
                val_tich_vh_ab_ac = '0'
                val_cos = '-\\frac{1}{2}'
            elif kich_ban == '90_deg':
                # Giả thiết: Tất cả các cạnh đều bằng a (tứ diện đều)
                val_BC = '%s' % (latex(val_a))
                goc_kq = 90
                text_tam_giac_abc = 'đều (do $AB=AC=BC=%s$)' % (latex(val_a))
                val_tich_vh_ab_ac = '%s^2 \\cdot \\cos 60^\\circ = \\frac{%s^2}{2}' % (latex(val_a), latex(val_a))
                val_cos = '0'

            # B4: Điều chỉnh các phương án sai (không trùng đáp án đúng)
            da_dung = '$%s^\\circ$' % (goc_kq)
            cac_lua_chon_sai = ['$30^\\circ$', '$60^\\circ$', '$90^\\circ$', '$45^\\circ$', '$120^\\circ$', '$150^\\circ$']
            random.shuffle(cac_lua_chon_sai)
            list_sai = [s for s in cac_lua_chon_sai if s != da_dung][:3]
            da_s1, da_s2, da_s3 = list_sai

            # B2: Viết lại nội dung bài toán
            noidungcauhoi = (
                'Cho hình chóp $S.ABC$ có $BC = %s$, các cạnh còn lại đều bằng $%s$. '
                'Góc giữa hai vectơ $\\vec{SB}$ và $\\vec{AC}$ bằng'
                % (val_BC, latex(val_a))
            )

            # TikZ vẽ hình
            venhinh = (
                '\\begin{center}\n'
                '\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round]\n'
                '\\coordinate[label=left:$A$] (A) at (0,0);\n'
                '\\coordinate[label=below:$B$] (B) at (1.5,-1.5);\n'
                '\\coordinate[label=right:$C$] (C) at (4,0);\n'
                '\\coordinate[label=above:$S$] (S) at (2.5,3);\n'
                '\\draw (S)--(A) (S)--(B) (S)--(C) (A)--(B) (B)--(C);\n'
                '\\draw[dashed] (A)--(C);\n'
                '\\end{tikzpicture}\n'
                '\\end{center}'
            )

            da_d = '\\True ' + da_dung
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Lời giải chi tiết theo kịch bản
            loigiai = (
                venhinh +
                'Xét tam giác $ABC$ có $AB=AC=%s$ và $BC=%s$. \\\\'
                'Suy ra tam giác $ABC$ %s. \\\\'
                'Do đó $\\vec{AB} \\cdot \\vec{AC} = %s$. \\\\'
                'Mặt khác, tam giác $SAC$ có $SA=SC=AC=%s$ nên là tam giác đều, suy ra $\\widehat{SAC} = 60^\\circ$. \\\\'
                'Ta tính tích vô hướng của hai vectơ $\\vec{SB}$ và $\\vec{AC}$ như sau: \\\\'
                '$\\vec{SB} \\cdot \\vec{AC} = (\\vec{SA} + \\vec{AB}) \\cdot \\vec{AC} = \\vec{SA} \\cdot \\vec{AC} + \\vec{AB} \\cdot \\vec{AC}$. \\\\'
                'Trong đó: \\\\'
                '$\\vec{SA} \\cdot \\vec{AC} = -\\vec{AS} \\cdot \\vec{AC} = -|\\vec{AS}| \\cdot |\\vec{AC}| \\cdot \\cos 60^\\circ = -\\frac{%s^2}{2}$. \\\\'
                'Khi đó: $\\vec{SB} \\cdot \\vec{AC} = -\\frac{%s^2}{2} + %s$. \\\\'
                'Suy ra $\\cos(\\vec{SB}, \\vec{AC}) = \\frac{\\vec{SB} \\cdot \\vec{AC}}{|\\vec{SB}| \\cdot |\\vec{AC}|} = %s$. \\\\'
                'Vậy góc giữa hai vectơ $\\vec{SB}$ và $\\vec{AC}$ bằng $%s^\\circ$.'
                % (latex(val_a), val_BC, text_tam_giac_abc, val_tich_vh_ab_ac, latex(val_a), 
                   latex(val_a), latex(val_a), val_tich_vh_ab_ac, val_cos, goc_kq)
            )

            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

