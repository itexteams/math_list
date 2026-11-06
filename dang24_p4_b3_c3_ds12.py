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


def bt_dang24_p4_b3_c3_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                a1=randint(70,90)
                a=a1/10
                b1=randint(95,120)
                b=b1/10
                c1=randint(21,30)
                h=c1/10
                d1=randint(51,60)
                R=d1/10
                e1=randint(30,40)
                r=e1/10
                f=R-sqrt(R**2-r**2)
                v1=(h/3)*(a**2+b**2+a*b)
                oi1=sqrt(R**2-r**2)
                oi=R**2-r**2
                v2=math.pi*f**2*(R-f/3)
                kq1=v1-v2
                number = Decimal(float(kq1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)


                # Nội dung câu hỏi
                noidungcauhoi = ('Để đặt một vật trang trí lên mặt bàn, người ta thiết kế một chân đế như sauzzz Lấy một khối gỗ có dạng khối chóp cụt tứ giác đều với độ dài hai đáy lần lượt bằng $%s$ cm và $%s$ cm,'
                                ' bề dày của khối gỗ bằng $%s$ cmzzz Sau đó khoét bỏ đi một phần của khối gỗ sao cho phần đó có dạng vật thể $H$, ở đó $H$ nhận được bằng cách cắt khối cầu có bán kính $%s$ cm bởi một'
                                ' mặt phẳng cắt mà mặt cắt là hình tròn bán kính $%s$ cm (xem hình dưới)zzz'
                                '''\\begin{center}
                                \\begin{tabular}{ccc}
            \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick,scale=0zzz6]
                \\coordinate (A) at (0,0);
                \\coordinate (B) at (-1zzz5,-1);
                \\coordinate (D) at (4,0);
                \\coordinate (C) at ($(B)+(D)-(A)$);
                \\coordinate (O) at ($(A)!0zzz42!(C)$);
                \\coordinate (I) at ($(O)+(0,3zzz5)$);
                \\coordinate (A') at ([scale around={0zzz71:(I)}] A);
                \\coordinate (B') at ([scale around={0zzz71:(I)}] B);
                \\coordinate (C') at ([scale around={0zzz71:(I)}] C);
                \\coordinate (D') at ([scale around={0zzz71:(I)}] D);
                \\coordinate (O') at ($(A')!0zzz5!(C')$);
                \\draw(B)--(C)--(D)--(D')--(C')--(B')--(A')--(D') (C)--(C') (B)--(B');
                \\draw[dashed,thin](A')--(A)--(B) (A)--(D);
                \\draw[dashed,<->](O)--(O')node[right,pos=0zzz1]{\\tiny $%s$cm};
                \\coordinate (vt) at (0,0zzz2);
                \\coordinate (A1) at ($(A')+(vt)$);
                \\coordinate (D1) at ($(D')+(vt)$);
                \\draw[|<->|](A1)--(D1)node[above,sloped,pos=0zzz5]{\\tiny $%s$cm};
                \\coordinate (vt1) at (0,0zzz1);
                \\coordinate (B1) at ($(B)-(vt)$);
                \\coordinate (C1) at ($(C)-(vt)$);
                \\draw[|<->|](B1)--(C1)node[below,sloped,pos=0zzz5]{\\tiny $%s$cm};
            \\end{tikzpicture}\\qquad
            \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick,scale=0zzz6]
                \\def\\bk{3}
                \\def\\bkba{0zzz15}
                \\def\\bkbb{0zzz8}
                \\def\\ga{-50}
                \\def\\gb{180-\\ga}
                \\def\\gc{0-\\gb}
                \\coordinate (O) at (0,0);
                \\coordinate (M) at ($(O) + (\\ga:\\bk)$);
                \\coordinate (N) at ($(O) + (\\gb:\\bk)$);
                \\coordinate (I) at ($(M)!0zzz5!(N)$);
                \\draw[name path=c1,dashed] (M) arc (\\ga:\\gb:\\bk);
                \\path let \\p1=(I),\\p2=(M),\\n1={scalar(veclen(\\x2-\\x1,\\y2-\\y1)/1cm)} in \\pgfextra{\\xdef\\bke{\\n1}};
                \\fill[gray](M) arc (\\ga:\\gc:\\bk)--(N) arc (180:0:\\bke cm and \\bkba cm)--cycle;
                \\draw[name path=c1] (M) arc (\\ga:\\gc:\\bk);
                \\draw[name path=ne1] (M) arc (0:180:\\bke cm and \\bkba cm);
                \\draw[name path=ne1] (M) arc (0:-180:\\bke cm and \\bkba cm);
                \\draw[name path=ela,dashed] (O) ellipse (\\bk cm and \\bkbb cm) ($(O)-(\\bk,0)$)--($(O)+(\\bk,0)$) (M)--(N);
                \\coordinate (P) at ($(O) + (250:0zzz9*\\bk)$);
                \\coordinate (Q) at ($(O) + (235:1zzz1*\\bk)$);
                \\path(Q) node [left] {\\Large\\bf H};
                \\draw[->](Q)--(P);
            \\end{tikzpicture}\\qquad
            \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick,rotate=90,scale=0zzz6]
                \\def\\bk{3}
                \\def\\bkba{0zzz15}
                \\def\\bkbb{0zzz8}
                \\def\\ga{-50}
                \\def\\gb{180-\\ga}
                \\def\\gc{0-\\gb}
                \\coordinate (O) at (0,0);
                \\coordinate (M) at ($(O) + (\\ga:\\bk)$);
                \\coordinate (N) at ($(O) + (\\gb:\\bk)$);
                \\coordinate (I) at ($(M)!0zzz5!(N)$);
                \\coordinate (J) at ($(O)+(M)-(I)$);
                \\draw(M) arc (\\ga:\\gb:\\bk);
                \\path let \\p1=(I),\\p2=(M),\\n1={scalar(veclen(\\x2-\\x1,\\y2-\\y1)/1cm)} in \\pgfextra{\\xdef\\bke{\\n1}};
                \\fill[gray](M) arc (\\ga:-90:\\bk)--(I)--cycle;
                \\draw(M) arc (\\ga:\\gc:\\bk);
                \\draw(M) arc (0:180:\\bke cm and \\bkba cm);
                \\draw[dashed](M) arc (0:-180:\\bke cm and \\bkba cm);
                \\coordinate (P) at ($(O) + (250:0zzz9*\\bk)$);
                \\coordinate (Q) at ($(O) + (235:1zzz1*\\bk)$);
                \\path(Q) node [below] {\\Large\\bf H};
                \\coordinate (A) at ($(O) + (180:\\bk)$);
                \\coordinate (B) at ($(O) + (0:\\bk)$);
                \\coordinate (C) at ($(O) + (-90:\\bk)$);
                \\coordinate (D) at ($(O) + (90:\\bk)$);
                \\draw(B) arc (0:180:\\bk cm and \\bkbb cm);
                \\draw[dashed](B) arc (0:-180:\\bk cm and \\bkbb cm);
                \\draw[dashed](J)--(M)--(N) (C)--(D) (A)--(B);
                \\draw[->](Q)--(P);
                \\draw[->](C)--($(C)-(0,0zzz5)$)node[below]{$x$};
                \\draw[->](B)--($(B)+(0zzz5,0)$)node[right]{$y$};
                \\draw(A)--($(A)-(0.5,0)$) (D)--($(D)+(0,0zzz5)$);
                \\path(O) node[below left]{$O$};
                \\path(J) node[left=-2]{\\tiny $%s$};
                \\path($(B)+(0zzz15,0)$)node[left]{\\tiny $%s$};
            \\end{tikzpicture}
            \\end{tabular}
            \\end{center}'''
            'Thể tích của khối chân đế bằng bao nhiêu centimét khối (\\textit{không làm tròn kết quả các phép tính trung gian, chỉ làm tròn kết quả cuối cùng đến hàng phần mười})?'
                                %(latex(a),latex(b),latex(h),latex(R),latex(r),
                                latex(h),latex(a),latex(b),latex(r),latex(R),
                                ))

                # Nội dung lời giải
                loigiai = ('Thể tích khối gỗ $V_1=\\dfrac{%s}{3}\\left(%s^2+%s^2+\\sqrt{%s^2\\cdot%s^2}\\right)$ (cm$^3$)zzz \\\\ \n'
                        'Gọi $I$ là tâm đường tròn mặt cắt và $M$ là một điểm trên đường tròn nàyzzz'
                        '$$OI=\\sqrt{OM^2-MI^2}=\\sqrt{%s^2-%s^2}=\\sqrt{%s}zzz$$'
                        'Mặt phẳng $(Oxy)$ cắt mặt cầu theo đường tròn tâm $O$ bán kính $%s$ cm nên đường tròn này có phương trình $x^2+y^2=%s^2 \\Rightarrow y^2=-x^2+%s^2$zzz\\\\ \n'
                        'Thể tích $(H)$ là $V_2=\\pi \\displaystyle \\int\\limits_{\\sqrt{%s}}^{%s}\\left(-x^2+%s^2\\right)\\text{d}x$ (cm$^3$)zzz\\\\ \n'
                        'Thể tích khối chân đế $V=V_1-V_2$'
                        '$$\\dfrac{%s}{3}\\left(%s^2+%s^2+\\sqrt{%s^2\\cdot%s^2}\\right)-\\pi \\displaystyle \\int\\limits_{\\sqrt{%s}}^{%s}\\left(-x^2+%s^2\\right)\\text{d}x \\approx %s\\text{ cm}^3zzz$$'

                        %(latex(h),latex(a),latex(b),latex(a),latex(b),
                            latex(R),latex(r),latex(oi),
                            latex(R),latex(R),latex(R),
                            latex(oi),latex(R),latex(R),
                            latex(h),latex(a),latex(b),latex(a),latex(b),latex(oi),latex(R),latex(R),latex(kq),
                        ))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.0','').replace('.', ',').replace('zzz','.')
            return content

