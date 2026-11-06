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


def bt_dang6_p3_b1_c1_hh12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                p1=randint(6,15)
                p=p1*3
                a=randint(50,70)
                r=a/100
                t=randint(5,30)
                while t**2-p1**2<=0:
                    p1=randint(6,15)
                    p=p1*3
                    a=randint(50,70)
                    r=a/100
                    t=randint(5,30)

                d1=sqrt(((r**2)*(t**2))/(t**2-p1**2))
                number = Decimal(float(d1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('\\immini{'
                                'Một chiếc đèn được treo song song với mặt phẳng nằm ngang bởi ba sợi dây không giãn xuất phát từ điểm $O$ '
                                'trên trần nhà và lần lượt buộc vào ba điểm $A,B,C$ trên đèn tròn sao tam giác $ABC$ đều$zz$ Độ dài của ba đoạn thẳng $OA,OB,OC$ đều bằng $L$$zz$ '
                                'Trọng lượng của chiếc đèn là $%s$N và bán kính của đèn là $%s$m$zz$ Tìm chiều dài tối thiểu của mỗi sợi dây, biết rằng mỗi sợi dây đó được thiết kế để chịu được lực căng tối đa là $%s$$zz$ (Chiều dài tính theo đơn vị cm và làm tròn đến hàng phần chục)$zz$'

                                '}{'
                                '''
                                \\definecolor{ffqqqq}{rgb}{1$zz$,0$zz$,0$zz$}
                                '\\scalebox{0$zz$6}{ '
            \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                \\clip(-3$zz$5018443859090067,-3$zz$2594319584779825) rectangle (3$zz$5903951362890627,5$zz$807509548332079);
                \\fill[line width=1$zz$pt,fill=black,pattern=north east lines,pattern color=black] (-2$zz$,5$zz$) -- (2$zz$,5$zz$) -- (2$zz$0139205045277446,5$zz$408017981662814) -- (-2$zz$006279438536401,5$zz$408017981662814) -- cycle;
                \\draw [rotate around={0$zz$:(0$zz$,0$zz$)},line width=1$zz$pt] (0$zz$,0$zz$) ellipse (2$zz$2882456112707374cm and 1$zz$111785940502843cm);
                \\draw [line width=1$zz$pt] (-2$zz$2882456112707374,0$zz$)-- (-2$zz$275131461388665,-0$zz$5664988543722905);
                \\draw [line width=1$zz$pt] (2$zz$2882456112707374,0$zz$)-- (2$zz$2813454189935207,-0$zz$6201044647297278);
                \\draw [shift={(0$zz$03194986111782334,1$zz$8583433372576157)},line width=1$zz$pt]  plot[domain=3$zz$9518721504673895:5$zz$449377484002473,variable=\\t]({1$zz$*3$zz$3470111865613497*cos(\\t r)+0$zz$*3$zz$3470111865613497*sin(\\t r)},{0$zz$*3$zz$3470111865613497*cos(\\t r)+1$zz$*3$zz$3470111865613497*sin(\\t r)});
                \\draw [line width=1$zz$pt,dash pattern=on 3pt off 3pt] (0$zz$,0$zz$)-- (2$zz$2882456112707374,0$zz$);
                \\draw [line width=1$zz$pt,dash pattern=on 3pt off 3pt] (0$zz$,0$zz$)-- (0$zz$,-1$zz$4885153525202133);
                \\draw [line width=1$zz$pt] (0$zz$,5$zz$)-- (2$zz$2882456112707374,0$zz$);
                \\draw [line width=1$zz$pt] (0$zz$,5$zz$)-- (-2$zz$1157654381919273,-0$zz$42345993765770873);
                \\draw [line width=1$zz$pt] (0$zz$,5$zz$)-- (-1$zz$,1$zz$);
                \\draw [->,line width=1$zz$pt,color=ffqqqq] (0$zz$,-1$zz$4885153525202133) -- (0$zz$,-3$zz$);
                \\draw [->,line width=1$zz$pt,color=ffqqqq] (0$zz$,5$zz$) -- (1$zz$2585378940871805,2$zz$249993864539145);
                \\draw [->,line width=1$zz$pt,color=ffqqqq] (0$zz$,5$zz$) -- (-0$zz$6132180805615,2$zz$5471276777540033);
                \\draw [->,line width=1$zz$pt,color=ffqqqq] (0$zz$,5$zz$) -- (-1$zz$2428238823280127,1$zz$81419999887589);
                \\draw [line width=1$zz$pt] (-2$zz$,5$zz$)-- (2$zz$,5$zz$);
                \\draw [line width=1$zz$pt] (2$zz$,5$zz$)-- (2$zz$0139205045277446,5$zz$408017981662814);
                \\draw [line width=1$zz$pt] (2$zz$0139205045277446,5$zz$408017981662814)-- (-2$zz$006279438536401,5$zz$408017981662814);
                \\draw [line width=1$zz$pt] (-2$zz$006279438536401,5$zz$408017981662814)-- (-2$zz$,5$zz$);
                \\draw (-0$zz$8040120970728782,5) node[anchor=north west] {$O$};
                \\draw (-1$zz$9582393134306033,2$zz$720299403375279) node[anchor=north west] {$\\vec{F}_1$};
                \\draw (-0$zz$5397914089909894,3$zz$2765534835476755) node[anchor=north west] {$\\vec{F}_2$};
                \\draw (1$zz$2402216475606829,3$zz$1653026675131963) node[anchor=north west] {$\\vec{F}_3$};
                \\draw (-2$zz$1390218894866324,0$zz$20324969059518536) node[anchor=north west] {$A$};
                \\draw (-1$zz$1377645451763168,1$zz$204507034905499) node[anchor=north west] {$B$};
                \\draw (2$zz$3110107518925482,0$zz$5091894346900033) node[anchor=north west] {$C$};
                \\draw (0$zz$016462671181408168,-2$zz$2581746141676686) node[anchor=north west] {$\\vec{P}$};
            \\end{tikzpicture}}
                                '''
                                '}'

                                %(latex(p),latex(r),latex(t))
                                )

                # Nội dung lời giải
                loigiai = ('Gọi $G$ là trọng tâm của tam giác $ABC$$zz$\\\\ \n'
                        'Vì tam giác $ABC$ đều nên $G$ là tâm đường tròn ngoại tiếp tam giác $ABC$\\\\ \n'
                        'Do đó, $GA=GB=GC=%s$m$zz$\\\\ \n'
                        'Gọi $F$ là độ lớn của các lực căng $\\vec{F_1},\\vec{F_2},\\vec{F_3}$ trên mỗi sợi dây$zz$ Khi đó, $F=F(L)$ là một hàm số đối với biến $L$$zz$\\\\ \n'
                        'Theo bài ra ta có $OA=OB=OC=L$ nên $OG\\perp (ABC)$ và $\\abs{\\vec{OA}}=\\abs{\\vec{OB}}=\\abs{\\vec{OC}}=L$$zz$\\\\ \n'
                        'Do đó  $\\abs{\\vec{F_1}}=\\abs{\\vec{F_2}}=\\abs{\\vec{F_3}}$$zz$\\\\ \n'
                        'Vì vậy, tồn tại hằng số $c\\neq 0$ sao cho $\\vec{F_1}=c\\vec{OA}, \\vec{F_2}=c\\vec{OB}, \\vec{F_3}=c\\vec{OC}$$zz$\\\\ \n'
                        'Suy ra $\\vec{F_1}+\\vec{F_2}+\\vec{F_3}=c\\left(\\vec{OA}+\\vec{OB}+\\vec{OC}\\right)$$zz$\\\\ \n'
                        'Vì $G$ là trọng tâm của tam giác $ABC$ nên ta có  $\\vec{OA}+\\vec{OB}+\\vec{OC}=3\\vec{OC}$$zz$\\\\ \n'
                        'Do đó $\\vec{F_1}+\\vec{F_2}+\\vec{F_3}=3c\\vec{OG}$$zz$\\\\ \n'
                        'Mặt khác ta lại có $\\vec{F_1}+\\vec{F_2}+\\vec{F_3}=\\vec{P}$, với $\\vec{P}$ là trọng lực tác dụng lên chiếc đèn$zz$\\\\ \n'
                        'Mà trọng lực tác dụng lên chiếc đèn là $%s$N nên $\\abs{\\vec{P}}=%s \\Leftrightarrow 3c\\abs{\\vec{OG}}=%s\\Leftrightarrow c=\\dfrac{%s}{OG}$$zz$\\\\ \n'
                        'Tam giác $OAG$ vuông tại $G$ nên suy ra $OG=\\sqrt{OA^2-GA^2}=\\sqrt{L^2-%s^2}$(m) với $L>%s$$zz$\\\\ \n'
                        'Do đó $\\abs{OG}=\\sqrt{L^2-%s^2} \\Rightarrow c=\\dfrac{%s}{\\sqrt{L^2-%s^2}}$$zz$\\\\ \n'
                        'Khi đó $\\abs{\\vec{F}}=\\abs{\\vec{F_1}}=c\\abs{\\vec{OA}}=\\dfrac{%sL}{\\sqrt{L^2-%s^2}}$ (với $L>%s$)$zz$\\\\ \n'
                        'Ta có lực căng dây tối đa của mỗi sợi dây là $%s$N\\\\ \n'
                        '\\hspace*{1cm}$F(L)\\leq %s \\Leftrightarrow \\dfrac{%sL}{\\sqrt{L^2-%s^2}}\\leq %s$\\\\ \n'
                        '\\hspace*{1cm}$\\Leftrightarrow %sL\\leq %s\\sqrt{L^2-%s^2} \\Leftrightarrow %sL^2\\leq %s(L^2-%s^2) \\Leftrightarrow %sL^2\\leq -%s\\Rightarrow L \\geq %s$$zz$\\\\ \n'
                        'Vậy chiều dài tối thiểu của mỗi sợi dây là $L=%s\\text{m}=%s$cm$zz$'
                        %(latex(r), latex(p),latex(p),latex(p),latex(p1),latex(r), latex(r),latex(r), latex(p1), latex(r),latex(p1), latex(r),
                        latex(r),latex(t),latex(t),latex(p1), latex(r),latex(t),latex(p1),latex(t),latex(r),latex(p1**2),latex(t**2),latex(r),latex(-t**2+p1**2),latex((t**2)*r**2),latex(kq),latex(kq),latex(kq*100)
                        )
                            )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq*100))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.')
            return content

