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


def bt_dang68_p3_b1_c2_hh11(self):
            # Khai báo biến
            list_canh = ['a', 'b', 'x', 's']
            c = random.choice(list_canh)
            canh = symbols(c)

            # Tính toán các đại lượng
            # DM = DN = a*sqrt(3)/2 (đường cao tam giác đều)
            # MN = a/2 (đường trung bình)
            dm_val = (canh * sqrt(3)) / 2
            dn_val = dm_val
            mn_val = canh / 2

            # Cosin góc giữa DM và MN (cũng là cosin góc giữa DM và AB)
            # cos = (DM^2 + MN^2 - DN^2) / (2 * DM * MN)
            tu = dm_val**2 + mn_val**2 - dn_val**2
            mau = 2 * dm_val * mn_val
            cos_val = tu / mau # Kết quả luôn là sqrt(3)/6

            # B4: Điều chỉnh các phương án sai
            da_dung = '$%s$' % (latex(cos_val))

            # Tạo danh sách các phương án nhiễu thường gặp trong hình học 11-12
            s = [
                '$%s$' % (latex(sqrt(3)/2)),
                '$%s$' % (latex(sqrt(3)/3)),
                '$%s$' % (latex(Rational(1, 2))),
                '$%s$' % (latex(sqrt(2)/2)),
                '$%s$' % (latex(sqrt(6)/6)),
                '$%s$' % (latex(Rational(1, 3)))
            ]

            # Loại bỏ đáp án đúng nếu lỡ trùng trong danh sách nhiễu
            if da_dung in s:
                s.remove(da_dung)

            random.shuffle(s)
            das1 = s[0]
            das2 = s[1]
            das3 = s[2]

            # TikZ Code (Hình vẽ chính xác như trong ảnh)
            tikz_code = (
                '\\begin{center}\n'
                '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round]\n'
                '   \\coordinate (A) at (0,0);\n'
                '   \\coordinate (B) at (1.2,-1.2);\n'
                '   \\coordinate (C) at (3.5,0);\n'
                '   \\coordinate (D) at (1.75,3);\n'
                '   \\coordinate (M) at ($(B)!0.5!(C)$);\n'
                '   \\coordinate (N) at ($(A)!0.5!(C)$);\n'
                '   \\draw (D)--(A)--(B)--(C)--(D)--(B) (D)--(M);\n'
                '   \\draw[dashed] (A)--(C) (D)--(N)  (M)--(N);\n'
                '   \\tkzDrawPoints[fill=black](A,B,C,D,M,N)\n'
                '   \\tkzLabelPoints[left](A)\n'
                '   \\tkzLabelPoints[right](C)\n'
                '   \\tkzLabelPoints[below](B,M)\n'
                '   \\tkzLabelPoints[above](D)\n'
                '   \\tkzLabelPoints[above left](N)\n'
                '   \\tkzMarkRightAngle[size=0](D,N,C)\n'
                '   \\tkzMarkRightAngle[size=0](D,M,B)\n'
                '\\end{tikzpicture}\n'
                '\\end{center}'
            )

            # B2: Viết lại nội dung câu hỏi
            noidungcauhoi = (
                'Cho tứ diện đều $ABCD$ cạnh $%s$. Gọi $M$ là trung điểm của $BC$. '
                'Cosin của góc giữa hai đường thẳng $AB$ và $DM$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).'
                % (latex(canh))
            )

            # Đáp án
            da_d = ('\\True ' + str(da_dung))
            list_ans = [da_d, das1, das2, das3]
            random.shuffle(list_ans)

            # Lời giải chi tiết
            h1=sqrt(3)/6
            number = Decimal(float(h1))  # Số cần làm tròn
            kqz = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            loigiai = (
                'Gọi $N$ là trung điểm của $AC$. Khi đó, $MN$ là đường trung bình của tam giác $ABC$ nên $MN \\parallel AB$.\\\\'
                'Do đó, góc giữa hai đường thẳng $AB$ và $DM$ chính là góc giữa hai đường thẳng $MN$ và $DM$.\\\\'
                'Ta có $(DM, AB) = (DM, MN)$.\\\\'
                'Xét tứ diện đều cạnh $%s$, ta có $DM$ và $DN$ là hai đường cao của hai mặt tam giác đều bằng nhau.\\\\'
                'Dễ dàng tính được $DM = DN = \\frac{%s\\sqrt{3}}{2}$ và $MN = \\frac{%s}{2}$.\\\\'
                'Trong tam giác $DMN$, áp dụng hệ quả định lý cosin, ta có:\\\\'
                '$\\cos \\widehat{DMN} = \\frac{DM^2 + MN^2 - DN^2}{2 \\cdot DM \\cdot MN} = \\frac{\\left(\\frac{%s\\sqrt{3}}{2}\\right)^2 + \\left(\\frac{%s}{2}\\right)^2 - \\left(\\frac{%s\\sqrt{3}}{2}\\right)^2}{2 \\cdot \\frac{%s\\sqrt{3}}{2} \\cdot \\frac{%s}{2}} = \\frac{\\frac{%s^2}{4}}{\\frac{%s^2\\sqrt{3}}{2}} = \\frac{\\sqrt{3}}{6}$.\\\\'
                'Vì $\\cos \\widehat{DMN} = \\frac{\\sqrt{3}}{6} > 0$ nên $\\cos (DM, MN) = \\frac{\\sqrt{3}}{6}$.\\\\'
                'Vậy $\\cos (DM, AB) = \\frac{\\sqrt{3}}{6} \\approx %s$.'
                % (latex(canh), latex(canh), latex(canh), latex(canh), latex(canh), latex(canh), latex(canh), latex(canh), latex(canh), latex(canh),str(kqz))
            )

            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(str(kqz).replace('.',','))

            # Xuất câu trắc nghiệm (B1 & B2)
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{\n' + tikz_code + '\n' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

