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


def bt_dang8_p3_b4_c2_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':

        factor = choice([1, 2, 3])
        l_val = choice([2, 3, 4, 5]) * factor
        L_val = 2 * l_val

        c_val = choice([l_val, l_val + 1, l_val + 2])


        SA_val = 2 * c_val


        SM2 = 4 * (c_val ** 2) - (l_val ** 2)
        MN2 = L_val ** 2
        cos_phi = abs(2 * SM2 - MN2) / (2 * SM2)

        # Tính số đo góc theo độ
        angle_rad = math.acos(float(cos_phi))
        angle_deg = math.degrees(angle_rad)

        # Làm tròn đến hàng phần mười
        number = Decimal(str(angle_deg))
        kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình chóp cụt tứ giác đều $ABCD.A'B'C'D'$ có đáy lớn $ABCD$, đáy nhỏ $A'B'C'D'$. Biết $AB = %sa$, $C'D' = %sa$, $AA' = %sa$ ($a > 0$). Tính góc giữa hai mặt phẳng $(ABB'A')$ và $(CDD'C')$. Kết quả làm tròn đến hàng phần mười độ.'''
                         % (str(L_val), str(l_val), str(c_val)))

        # Hình vẽ TikZ
        hinhve = '''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (5,0);
    \\coordinate (D) at (-1.5,-1.8);
    \\coordinate (C) at (3.5,-1.8);
    \\coordinate (O) at (1.75,-0.9);
    \\coordinate (S) at (1.75,4.5);
    \\coordinate (A') at ($(S)!0.5!(A)$);
    \\coordinate (B') at ($(S)!0.5!(B)$);
    \\coordinate (C') at ($(S)!0.5!(C)$);
    \\coordinate (D') at ($(S)!0.5!(D)$);
    \\coordinate (M) at ($(A)!0.5!(B)$);
    \\coordinate (N) at ($(C)!0.5!(D)$);
    \\coordinate (M') at ($(A')!0.5!(B')$);
    \\coordinate (N') at ($(C')!0.5!(D')$);
    \\draw[line width=1pt] (D)--(C)--(B) (D)--(D') (C)--(C') (B)--(B') (D')--(C')--(B')--(A')--(D');
    \\draw[line width=1pt, dashed] (A)--(D) (A)--(B) (A)--(A') (S)--(A') (S)--(B) (S)--(C) (S)--(D) (S)--(M) (S)--(N) (M)--(N);
    \\fill (A) circle (1pt) node[above left] {$A$};
    \\fill (B) circle (1pt) node[right] {$B$};
    \\fill (C) circle (1pt) node[below right] {$C$};
    \\fill (D) circle (1pt) node[below left] {$D$};
    \\fill (A') circle (1pt) node[above left] {$A'$};
    \\fill (B') circle (1pt) node[above right] {$B'$};
    \\fill (C') circle (1pt) node[below right] {$C'$};
    \\fill (D') circle (1pt) node[below left] {$D'$};
    \\fill (S) circle (1pt) node[above] {$S$};
    \\fill (M) circle (1pt) node[above left] {$M$};
    \\fill (N) circle (1pt) node[below] {$N$};
    \\end{tikzpicture}
    \\end{center}'''

        # Nội dung lời giải
        loigiai = ('''%s
                   Kéo dài các cạnh bên $AA', BB', CC', DD'$ cắt nhau tại đỉnh $S$. Do $ABCD.A'B'C'D'$ là hình chóp cụt tứ giác đều nên $S.ABCD$ là hình chóp tứ giác đều và đáy nhỏ $A'B'C'D'$ song song với đáy lớn $ABCD$. \\\\
                   Xét tam giác $SAB$ có $A'B' // AB$ và $\\dfrac{A'B'}{AB} = \\dfrac{%sa}{%sa} = \\dfrac{1}{2}$, suy ra $A'$ là trung điểm của $SA$. \\\\
                   Do đó, $SA = 2AA' = 2 \\cdot %sa = %sa$. \\\\
                   Gọi $O$ là tâm của đáy $ABCD$, suy ra $SO \\perp (ABCD)$. \\\\
                   Đáy $ABCD$ là hình vuông cạnh $%sa$ nên bán kính đường tròn ngoại tiếp đáy là: \\\\
                   $OA = \\dfrac{AB\\sqrt{2}}{2} = \\dfrac{%sa\\sqrt{2}}{2} = %sa\\sqrt{2}$. \\\\
                   Trong tam giác vuông $SOA$, ta có: \\\\
                   $SO^2 = SA^2 - OA^2 = (%sa)^2 - (%sa\\sqrt{2})^2 = %sa^2$. \\\\
                   Gọi $M, N$ lần lượt là trung điểm của $AB$ và $CD$. \\\\
                   Khi đó $OM = ON = \\dfrac{AB}{2} = %sa$ và $MN = %sa$. \\\\
                   Trong tam giác vuông $SOM$, ta có: \\\\
                   $SM = \\sqrt{SO^2 + OM^2} = \\sqrt{%sa^2 + (%sa)^2} = a\\sqrt{%s}$. \\\\
                   Do tính đối xứng, ta cũng có $SN = SM = a\\sqrt{%s}$. \\\\
                   Giao tuyến của hai mặt phẳng $(ABB'A')$ [chính là mặt phẳng $(SAB)$] và $(CDD'C')$ [chính là mặt phẳng $(SCD)$] là đường thẳng $d$ đi qua $S$ và song song với $AB, CD$. \\\\
                   Vì tam giác $SAB$ cân tại $S$ nên trung đoạn $SM \\perp AB \\Rightarrow SM \\perp d$. \\\\
                   Tương tự, tam giác $SCD$ cân tại $S$ nên trung đoạn $SN \\perp CD \\Rightarrow SN \\perp d$. \\\\
                   Do đó, góc giữa hai mặt phẳng $(ABB'A')$ và $(CDD'C')$ bằng góc giữa hai đường thẳng $SM$ và $SN$. \\\\
                   Áp dụng định lí côsin trong tam giác $SMN$, ta có: \\\\
                   $\\cos \\widehat{MSN} = \\dfrac{SM^2 + SN^2 - MN^2}{2 \\cdot SM \\cdot SN} = \\dfrac{%sa^2 + %sa^2 - (%sa)^2}{2 \\cdot a\\sqrt{%s} \\cdot a\\sqrt{%s}} = %s$. \\\\
                   Suy ra góc giữa hai mặt phẳng là $\\alpha \\approx %s^\\circ$.'''
                   % (hinhve,
                      str(l_val), str(L_val),
                      str(c_val), str(SA_val),
                      str(L_val),
                      str(L_val), str(l_val),
                      str(SA_val), str(l_val), str(4 * c_val**2 - 2 * l_val**2),
                      str(l_val), str(L_val),
                      str(4 * c_val**2 - 2 * l_val**2), str(l_val), str(SM2),
                      str(SM2),
                      str(SM2), str(SM2), str(L_val), str(SM2), str(SM2),
                      latex(Rational(2 * SM2 - MN2, 2 * SM2)),
                      str(kq_str)
                   ))

        # Đáp án
        dapan = '\\shortans[0]{$%s^\\circ$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' + '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) + '\\loigiai{ \n' + str(loigiai) + '}\n' + '\\end{ex}\n \\end{minipage} \n\n')
    return content

