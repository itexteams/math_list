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


def bt_dang15_p3_b1_c2_hh11(self):
            # Khai báo biến
            # Trong đề gốc, M là trung điểm nên k = 1/2.
            list_k = [
                (Rational(1, 2), "là trung điểm cạnh"),
                (Rational(1, 3), "thỏa mãn $CM = \\frac{1}{3}CC'$"),
                (Rational(2, 3), "thỏa mãn $CM = \\frac{2}{3}CC'$")
            ]

            k, text_m = random.choice(list_k)

            # Tính toán các giá trị dựa trên cạnh a (coi a = 1 để tính toán tỉ lệ)
            # AH = sqrt(3)/2, A'H = sqrt(3)/2 => AA' = sqrt(AH^2 + A'H^2) = sqrt(6)/2
            aa_prime = sqrt(6)/2
            cc_prime = aa_prime
            cm = k * cc_prime

            # BM = sqrt(BC^2 + CM^2) = sqrt(1^2 + cm^2)
            bm_sq = 1 + cm**2
            bm = sqrt(bm_sq)

            # Tích vô hướng AA'.BM = AA'.(BC + CM) = AA'.BC + AA'.CM
            # Vì AA' vuông góc BC nên AA'.BC = 0.
            # Vì AA' song song CC' nên AA'.CM = |AA'| * |CM|
            tich_vo_huong = aa_prime * cm

            # cos(alpha) = |AA'.BM| / (|AA'| * |BM|)
            cos_alpha = simplify(tich_vo_huong / (aa_prime * bm))

            # Đáp án đúng
            da_dung = "$%s$" % latex(cos_alpha)

            # Bước 4: Tạo các phương án sai (không trùng đáp án đúng)
            s = []
            distractors = [sqrt(11)/11, 2*sqrt(22)/11, sqrt(22)/11, sqrt(33)/11, sqrt(7)/7, sqrt(2)/3, sqrt(5)/5]
            for d in distractors:
                d_latex = "$%s$" % latex(simplify(d))
                if d_latex != da_dung:
                    s.append(d_latex)

            random.shuffle(s)
            das1, das2, das3 = s[:3]

            # Câu hỏi
            noidungcauhoi = ("Cho hình lăng trụ $ABC.A'B'C'$ có đáy $ABC$ là tam giác đều cạnh $a$, tam giác $A'BC$ đều nằm trong mặt phẳng vuông góc với $(ABC)$. $M$ là điểm thuộc cạnh $CC'$ %s $CC'$. Cosin góc $\\alpha$ giữa hai đường thẳng $AA'$ và $BM$ bằng bao nhiêu? (làm tròn kết quả đến hàng đơn vị)." % text_m)

            # Nội dung lời giải chi tiết
            h1=cos_alpha
            number = Decimal(float(h1))  # Số cần làm tròn
            kqz = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
            loigiai = (
                "Gọi $H$ là trung điểm của $BC$. Vì tam giác $A'BC$ đều và nằm trong mặt phẳng vuông góc với $(ABC)$ nên $A'H \\perp (ABC)$.\\\\ "
                "Ta có $AH$ và $A'H$ lần lượt là đường cao của các tam giác đều $ABC$ và $A'BC$ cạnh $a$, nên $AH = A'H = \\frac{a\\sqrt{3}}{2}$.\\\\ "
                "Xét tam giác vuông $A'HA$, ta có $AA' = \\sqrt{AH^2 + A'H^2} = \\sqrt{\\left(\\frac{a\\sqrt{3}}{2}\\right)^2 + \\left(\\frac{a\\sqrt{3}}{2}\\right)^2} = \\frac{a\\sqrt{6}}{2}$.\\\\ "
                "Vì $BC \\perp AH$ và $BC \\perp A'H$ nên $BC \\perp (AA'H) \\Rightarrow BC \\perp AA'$.\\\\ "
                "Mặt khác $AA' \\parallel CC'$ nên $BC \\perp CC'$, suy ra tứ giác $BCC'B'$ là hình chữ nhật.\\\\ "
                "Theo giả thiết, $CM = %s CC' = %s \\cdot \\frac{a\\sqrt{6}}{2} = %s$.\\\\ "
                "Trong tam giác vuông $BCM$, ta có $BM = \\sqrt{BC^2 + CM^2} = \\sqrt{a^2 + \\left(%s\\right)^2} = %s$.\\\\ "
                "Sử dụng tích vô hướng: $\\vec{AA'} \\cdot \\vec{BM} = \\vec{AA'} \\cdot (\\vec{BC} + \\vec{CM}) = \\vec{AA'} \\cdot \\vec{BC} + \\vec{AA'} \\cdot \\vec{CM}$.\\\\ "
                "Vì $AA' \\perp BC$ nên $\\vec{AA'} \\cdot \\vec{BC} = 0$. Vì $\\vec{AA'}$ cùng hướng $\\vec{CM}$ nên $\\vec{AA'} \\cdot \\vec{CM} = AA' \\cdot CM = \\frac{a\\sqrt{6}}{2} \\cdot %s = %s$.\\\\ "
                "Vậy $\\cos \\alpha = \\frac{|\\vec{AA'} \\cdot \\vec{BM}|}{AA' \\cdot BM} = \\frac{%s}{\\frac{a\\sqrt{6}}{2} \\cdot %s} = %s \\approx %s$."
                % (latex(k), latex(k), latex(cm*symbols('a')), 
                   latex(cm*symbols('a')), latex(bm*symbols('a')),
                   latex(cm*symbols('a')), latex(simplify(aa_prime * cm)*symbols('a')**2),
                   latex(simplify(aa_prime * cm)*symbols('a')**2), latex(bm*symbols('a')),
                   latex(cos_alpha), str(kqz))
            )

            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(latex(kqz))

            # TikZ Hình vẽ
            hinh_ve = r"""\begin{center}
            \begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (71.47,181.07) -- (180.47,181.07) ;
            	\draw [line width=1]    (71.47,181.07) -- (120.47,218.07) ;
            	\draw [line width=1]    (120.47,218.07) -- (180.47,181.07) ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (150.47,199.57) -- (150.47,71.07) ;
            	\draw [line width=1]    (71.47,181.07) -- (150.47,71.07) ;
            	\draw [line width=1]    (150.47,71.07) -- (255.47,71.07) ;
            	\draw [line width=1]    (180.47,181.07) -- (255.47,71.07) ;
            	\draw [line width=1]    (120.47,218.07) -- (195.47,112.07) ;
            	\draw [line width=1]    (150.47,71.07) -- (195.47,112.07) ;
            	\draw [line width=1]    (195.47,112.07) -- (255.47,71.07) ;
            	\draw [line width=1]    (150.47,71.07) -- (120.47,218.07) ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (150.47,71.07) -- (180.47,181.07) ;
            	\draw [line width=1]    (120.47,218.07) -- (217.97,126.07) ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (71.47,181.07) -- (150.47,199.57) ;
            	\draw (50,164) node [anchor=north west][inner sep=0.75pt]    {$A$};
            	\draw (113,220) node [anchor=north west][inner sep=0.75pt]    {$B$};
            	\draw (185,171) node [anchor=north west][inner sep=0.75pt]    {$C$};
            	\draw (137,46) node [anchor=north west][inner sep=0.75pt]    {$A'$};
            	\draw (187,84) node [anchor=north west][inner sep=0.75pt]    {$B'$};
            	\draw (259,55) node [anchor=north west][inner sep=0.75pt]    {$C'$};
            	\draw (150.47,199.57) node [anchor=north west][inner sep=0.75pt]    {$H$};
            	\draw (220,114) node [anchor=north west][inner sep=0.75pt]    {$M$};
            \end{tikzpicture}
            \end{center}"""

            # Xuất nội dung theo định dạng mẫu
            da_d = ('\\True ' + str(da_dung))
            list_1 = [da_d, str(das1), str(das2), str(das3)]
            random.shuffle(list_1)

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + hinh_ve+ str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

