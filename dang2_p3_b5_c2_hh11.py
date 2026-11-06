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


def bt_dang2_p3_b5_c2_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                a=randint(2,10)
                h=randint(2,10)
                a1=a*2
                a2=a1*2
                bc=a2
                ab=a1
                ac=nsimplify(a1*sqrt(3))
                ah=nsimplify(a*sqrt(3))
                ak=(ah*h)/(sqrt(ah**2+h**2))

                number = Decimal(float(ak))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho chóp $S$zz$ABC$ có đáy $ABC$ là tam giác vuông tại $A$, cạnh $BC=%s$, $\\widehat{ABC}=60^{\\circ}$$zz$ Cạnh $SA=%s$ và vuông góc với mặt phẳng đáy$zz$ Hỏi khoảng cách từ điểm $A$ đến mặt phẳng $(SBC)$ bằng bao nhiêu? (kết quả làm tròn đến hàng phần chục)$zz$'
                                %(latex(bc),latex(h))
                                )

                # Nội dung lời giải
                loigiai = (
                '\\begin{center}\n'
                '\\begin{tikzpicture}[scale=0$zz$8,>=stealth, font=\\footnotesize, line join=round, line cap=round]\n'
                '\\path\n'
                '(0,4) coordinate (S)\n'
                '(0,0) coordinate (A)\n'
                '(2,-2) coordinate (B)\n'
                '(6,0) coordinate (C)\n'
                '(4,-1) coordinate (H)\n'
                '(1$zz$98,1$zz$52) coordinate (K);\n'
                '\\draw (S)--(A)--(B)--(C)--(S)--(B);\n'
                '\\draw [dashed] (A)--(C);\n'
                '\\draw [dashed] (A)--(H);\n'
                '\\draw [dashed] (A)--(K);\n'
                '\\draw [dashed] (S)--(H);\n'
                '\\foreach \\d/\\g in{S/90,A/-90,B/-90,C/0,H/-45,K/45} \n' 
                '\\draw[fill=black](\\d)circle(0pt)node[shift={(\\g:0$zz$35)}]{$\\d$}; \n'
                '\\end{tikzpicture}\n'
                '\\end{center}\n'
                'Gọi $AH$ là đường cao của tam giác $ABC$ $(H \\in BC)$, $AK$ là đường cao của tam giác $SAH$ $(K \\in SH)$ ta có\\\\ \n'
                '$\\heva{&BC\\perp AH\\\\&BC\\perp SA}\\Rightarrow BC\\perp (SAH) \\Rightarrow BC\\perp AK$$zz$\\\\ \n'
                'Tương tự ta có $\\heva{&AK\\perp BC\\\\&AK\\perp SH}\\Rightarrow AK\\perp (SBC) \\Rightarrow d(A,(SBC))=AK$$zz$\\\\ \n'
                'Xét tam giác vuông $ABC$ có\\\\ \n'
                '$AB=BC\\cdot\\cos\\widehat{ABC}=%s\\cdot\\cos 60^{\\circ}=%s$$zz$\\\\ \n'
                '$AC=BC\\cdot\\sin\\widehat{ABC}=%s\\cdot\\cos 60^{\\circ}=%s$$zz$\\\\ \n'
                'Suy ra $AH=\\dfrac{AB\\cdot AC}{BC}=\\dfrac{%s\\cdot %s}{%s}=%s$$zz$\\\\ \n'
                'Xét tam giác vuông $SAH$ có đường cao $AK$ ta có\\\\ \n'
                '$AK=\\dfrac{SA\\cdot AH}{\\sqrt{SA^2+AH^2}}=\\dfrac{%s\\cdot %s}{\\sqrt{%s^2+(%s)^2}}\\approx%s$$zz$\\\\ \n'
                'Vậy $d(A,(SBC))\\approx %s$$zz$'


                        %(latex(bc),latex(ab),
                            latex(bc),latex(ac),
                            latex(ab),latex(ac),latex(bc),latex(ah),
                            latex(h),latex(ah),latex(h),latex(ah),latex(kq),latex(kq)
                            )
                            )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.')
            return content   

