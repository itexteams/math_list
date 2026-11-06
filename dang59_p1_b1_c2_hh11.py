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


def bt_dang59_p1_b1_c2_hh11(self):
            # Khai báo biến
            # Ta sẽ random độ dài cạnh đáy AB = a
            list_a = [1, 2, 3, 4, 5]
            a_val = random.choice(list_a)

            # Khai báo các ký hiệu dùng trong sympy
            a = a_val
            h = a * sqrt(2)

            # Tính toán các giá trị trong lời giải
            # AB' = sqrt(AB^2 + BB'^2) = sqrt(a^2 + 2a^2) = a*sqrt(3)
            # IB' = AB' / 2 = (a*sqrt(3))/2
            ib_prime = (a * sqrt(3)) / 2

            # B'M^2 = A'B'^2 + A'M^2 - 2*A'B'*A'M*cos(60)
            # B'M^2 = a^2 + (a/2)^2 - 2*a*(a/2)*(1/2) = 3a^2/4 => B'M = (a*sqrt(3))/2
            bm_prime = (a * sqrt(3)) / 2

            # IM = 1/2 * BC' = 1/2 * sqrt(BC^2 + CC'^2) = (a*sqrt(3))/2
            im = (a * sqrt(3)) / 2

            # --- BƯỚC 2: THIẾT LẬP ĐÁP ÁN ---
            da_dung = "$60^\\circ$"
            list_sai = ["$30^\\circ$", "$45^\\circ$", "$90^\\circ$", "$120^\\circ$"]
            random.shuffle(list_sai)
            da_s1, da_s2, da_s3 = list_sai[0], list_sai[1], list_sai[2]

            # --- BƯỚC 3: NỘI DUNG CÂU HỎI VÀ LỜI GIẢI ---
            noidungcauhoi = ("Cho lăng trụ đều $ABC.A'B'C'$ có $AB = %s$, $AA' = %s$. Góc giữa $AB'$ và $BC'$ bằng"
                             % (latex(a), latex(h)))

            # Vẽ hình bằng TikZ
            tikz_code = r"""\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw [line width=1]    (108.47,183.4) -- (268.47,183.4) ;
            	\draw [line width=1]    (108.47,63.4) -- (268.47,63.4) ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (108.47,183.4) -- (148.47,143.4) ;
            	\draw [line width=1]    (108.47,63.4) -- (148.47,23.4) ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (268.47,183.4) -- (148.47,143.4) ;
            	\draw [line width=1]    (268.47,63.4) -- (148.47,23.4) ;
            	\draw [line width=1]    (108.47,183.4) -- (108.47,63.4) ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (148.47,143.4) -- (148.47,23.4) ;
            	\draw [line width=1]    (268.47,183.4) -- (268.47,63.4) ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (148.47,143.4) -- (108.47,63.4) ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (268.47,183.4) -- (148.47,23.4) ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (148.47,143.4) -- (268.47,63.4) ;
            	\draw [line width=1]    (188.47,63.4) -- (148.47,23.4) ;
            	\draw [line width=1]    (208.47,103.4) -- (188.47,63.4) ;
            	\draw (277.85,194.6) node    {$A$};
            	\draw (151.23,159.2) node    {$B$};
            	\draw (102.31,195.6) node    {$C$};
            	\draw (277.85,60.6) node    {$A'$};
            	\draw (148.23,11.2) node    {$B'$};
            	\draw (97.31,60.6) node    {$C'$};
            	\draw (199.1,54.2) node    {$M$};
            	\draw (208.23,118.2) node    {$I$};
            \end{tikzpicture} """

            loigiai = ("Gọi $I$ là tâm của hình chữ nhật $ABB'A'$ và $M$ là trung điểm của $A'C'$. \\\\"
                       "Vì lăng trụ đã cho là lăng trụ đều nên đáy $ABC$ là tam giác đều cạnh $%s$ và các mặt bên là hình chữ nhật có chiều cao $h = %s$. \\\\"
                       "Xét tam giác $A'B'C'$ đều, có $M$ là trung điểm $A'C'$, ta có: \\\\"
                       "$B'M = \\sqrt{A'B'^2 + A'M^2 - 2A'B' \\cdot A'M \\cdot \\cos 60^\\circ} = \\sqrt{%s^2 + \\left(\\frac{%s}{2}\\right)^2 - 2 \\cdot %s \\cdot \\frac{%s}{2} \\cdot \\frac{1}{2}} = %s$. \\\\"
                       "Lại có $I$ là trung điểm $AB'$ nên $IB' = \\frac{1}{2}AB' = \\frac{1}{2}\\sqrt{AB^2+BB'^2} = \\frac{1}{2}\\sqrt{%s^2+(%s)^2} = %s$. \\\\"
                       "Mặt khác, $IM$ là đường trung bình của tam giác $AB'C'$ (hoặc chứng minh $IM \\parallel BC'$ qua tọa độ/vectơ), ta có $IM = \\frac{1}{2}BC' = \\frac{1}{2}\\sqrt{BC^2+CC'^2} = %s$. \\\\"
                       "Trong tam giác $MIB'$, ta thấy $IM = IB' = B'M = %s$, suy ra tam giác $MIB'$ đều. \\\\"
                       "Do đó $(AB', BC') = (AB', IM) = \\widehat{MIB'} = 60^\\circ$."
                       % (latex(a), latex(h), 
                          latex(a), latex(a), latex(a), latex(a), latex(bm_prime),
                          latex(a), latex(h), latex(ib_prime),
                          latex(im), latex(im)))

            # --- BƯỚC 4: XUẤT NỘI DUNG THEO MẪU ---
            list_ans = ["\\True " + da_dung, da_s1, da_s2, da_s3]
            random.shuffle(list_ans)

            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
                       '\\choice \n'
                       '{' + str(list_ans[0]) + '}\n'
                       '{' + str(list_ans[1]) + '}\n'
                       '{' + str(list_ans[2]) + '}\n'
                       '{' + str(list_ans[3]) + '}\n'
                       '\\loigiai{' '\\begin{center}\n' + tikz_code + '\n\\end{center}\n' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

