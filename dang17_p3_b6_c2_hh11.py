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


def bt_dang17_p3_b6_c2_hh11(self):
            # Khai báo biến
            # Random hệ số k cho cạnh a (AB = k*a, AC = k*a*sqrt(3))
            k = random.randint(1, 3)
            # Random giá trị m để SB = k*a*sqrt(m) sao cho SH là số đẹp
            list_m = [2, 5, 10, 17] 
            m_val = random.choice(list_m)

            a = symbols('a')

            # Tính toán các đại lượng
            ab = k
            ac = k * sqrt(3)
            bc = 2 * k
            bh = k
            sb = k * sqrt(m_val)
            sh = k * sqrt(m_val - 1)

            s_abc = simplify(Rational(1, 2) * ab * ac)
            vol = simplify(Rational(1, 3) * sh * s_abc)

            # --- BƯỚC 2: TẠO ĐÁP ÁN (CHUYỂN SANG SỐ THẬP PHÂN) ---
            def format_latex(expr):
                res = latex(expr).replace('.', ',')
                return res

            # Chuyển đổi thể tích sang số thập phân làm tròn đến hàng phần chục
            # Ta tính toán giá trị số (coefficient) đi kèm với a^3
            vol_numeric = float(vol.subs(a, 1).evalf())
            vol_rounded = round(vol_numeric, 1)

            # Định dạng kết quả cuối cùng: số thập phân + a^3
            str_vol_decimal = f"{vol_rounded}".replace('.', ',')
            da_dung = '$' + str_vol_decimal + '$'

            # Tạo các phương án nhiễu (cũng ở dạng thập phân)
            s1_val = round(vol_numeric * 3, 1)
            s1 = '$' + f"{s1_val}".replace('.', ',') + "a^3" + '$'

            s2_val = round(vol_numeric * 2, 1)
            s2 = '$' + f"{s2_val}".replace('.', ',') + "a^3" + '$'

            s3_val = round(vol_numeric * 0.5, 1) # Sai lệch hệ số
            s3 = '$' + f"{s3_val}".replace('.', ',') + "a^3" + '$'

            options = ['\\True ' + da_dung, s1, s2, s3]
            random.shuffle(options)

            # --- BƯỚC 3: DỰNG HÌNH TIKZ ---
            tikz_code = r"""\begin{center}
            \begin{tikzpicture}[scale=1, line join=round, line cap=round, line width=1pt]
                \coordinate (A) at (0,0);
                \coordinate (B) at (1.5,-1.5);
                \coordinate (C) at (4.5,0);
                \coordinate (H) at ($(B)!0.5!(C)$);
                \coordinate (S) at ($(H)+(0,4)$);
                \draw (S)--(A)--(B)--(C)--(S)--(B);
                \draw[dashed] (A)--(C) (S)--(H);
                \tkzMarkRightAngle[size=0.2](B,A,C)
                \tkzMarkRightAngle[size=0.2](S,H,C)
                \node[left] at (A) {$A$};
                \node[below left] at (B) {$B$};
                \node[right] at (C) {$C$};
                \node[below right] at (H) {$H$};
                \node[above] at (S) {$S$};
            \end{tikzpicture}
            \end{center}"""

            # --- BƯỚC 4: NỘI DUNG CÂU HỎI VÀ LỜI GIẢI ---
            str_ab = format_latex(ab)
            str_ac = format_latex(ac)
            str_sb = format_latex(sb)
            str_bc = format_latex(bc)
            str_bh = format_latex(bh)
            str_sh = format_latex(sh)
            str_sabc = format_latex(s_abc)

            noidungcauhoi = (
                "Cho hình chóp $S.ABC$ có đáy $ABC$ là tam giác vuông tại $A$. Hình chiếu của $S$ lên mặt phẳng "
                "$\\left(ABC\\right)$ là trung điểm $H$ của $BC$, $AB = " + str_ab + "$, $AC = " + str_ac + "$, "
                "$SB = " + str_sb + "$. Thể tích của khối chóp $S.ABC$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục)."
            )

            loigiai = (
                "Xét tam giác $ABC$ vuông tại $A$ có: $BC = \\sqrt{AB^2 + AC^2} = \\sqrt{\\left(" + str_ab + "\\right)^2 + "
                "\\left(" + str_ac + "\\right)^2} = " + str_bc + "$. \\\\"
                "$H$ là trung điểm của $BC$ nên $BH = " + str_bh + "$. \\\\"
                "Xét tam giác $SBH$ vuông tại $H$ có: $SH = \\sqrt{SB^2 - BH^2} = \\sqrt{\\left(" + str_sb + "\\right)^2 - "
                "\\left(" + str_bh + "\\right)^2} = " + str_sh + "$. \\\\"
                "Diện tích đáy $ABC$ là: $S_{ABC} = \\frac{1}{2} AB \\cdot AC = " + str_sabc + "$. \\\\"
                "Thể tích của khối chóp $S.ABC$ là: $V = \\frac{1}{3} SH \\cdot S_{ABC} = "
                "\\frac{1}{3} \\cdot " + str_sh + " \\cdot " + str_sabc + " \\approx " + str_vol_decimal + "$."
            )

            # Sử dụng kết quả đã làm tròn cho phần đáp án ngắn
            dapan = '\\shortans[0]{$%s$}\n' % (str_vol_decimal)

            # --- BƯỚC 5: XUẤT KẾT QUẢ ---
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' 
                + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + tikz_code+ str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

